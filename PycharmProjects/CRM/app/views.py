from utils.pagination import Pagination
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import auth
from .models import *
from app.forms import *
from django.views import View
from django.db.models import Q
from django.http import QueryDict
# transation——事务
from django.db import transaction
# 导入 settings
from django.conf import settings


# Create your views here
def first(request):
    return render(request, 'first.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj = auth.authenticate(request, username=username, password=password)
        # print(UserProfile.objects.get('username'))
        if obj:
            auth.login(request, obj)
            return redirect(reverse('my_customer'))
        err_mag = '用户名或密码错误'
        return render(request, 'login.html', {'err_msg': err_mag})
    return render(request, 'login.html')


def register(request):
    form_obj = RegForm()
    if request.method == 'POST':
        form_obj = RegForm(request.POST)
        if form_obj.is_valid():
            # form_obj.cleaned_data.pop('re_password')
            # # form_obj.cleaned_data.pop('re_password')
            # UserProfile.objects.create_user(**form_obj.cleaned_data)
            # return redirect('/login/')
            obj = form_obj.save()
            obj.set_password(obj.password)
            obj.save()
    return render(request, 'reg.html', {'form_obj': form_obj})


# 展示客户
# def customer_list(request):
#     if request.path_info == reverse('customer'):
#         all_customer = Customer.objects.filter(consultant__isnull=True)
#     else:
#         all_customer = Customer.objects.filter(consultant=request.user)
#         print()
#     # 如果长度为 0 是切不出来的
#     if all_customer.count() == 0:
#         return render(request, 'customer_list.html', )
#     p = Pagination(request, all_count=all_customer.count())
#     return render(
#         request, 'customer_list.html', {
#             'all_customer': all_customer[p.start:p.end],
#             'pagination': p.show_li,
#         })


# 测试分页
# 测试数据
# users = [{'name': '宋子良{}'.format(i), 'age': '{}'.format(i)}
#          for i in range(1, 207)]
#
#
# def user_list(request):
#     p = Pagination(request, all_count=len(users))
#     return render(request, 'user_list.html',
#                   {'test_data': users[p.start:p.end],
#                    'html_str': p.show_li}
#                   )
# 'show_page_range': p.show_page_range})


# 增加客户
# def add_customer(request):
#     # 实例化 form
#     form_obj = CustomerForm()
#     if request.method == 'POST':
#         form_obj = CustomerForm(request.POST)
#         # 对提交数据进行校验
#         if form_obj.is_valid():
#             # 校验成功
#             form_obj.save()
#             return redirect(to=reverse('customer'))
#     return render(request, 'add_customer.html', {'form_obj': form_obj})


# 客户编辑
# def edit_customer(request, edit_id):
#     # 根据 id 查出所需要编辑的客户
#     obj = models.Customer.objects.filter(id=edit_id).first()
#     # instance——实例
#     form_obj = CustomerForm(instance=obj)
#     if request.method == 'POST':
#         # 将提交的数据和要修改的实例交给 form 对象
#         form_obj = CustomerForm(request.POST, instance=obj)
#         if form_obj.is_valid():
#             form_obj.save()
#             return redirect(to=reverse('customer'))
#     return render(request, 'edit_customer.html', {'form_obj': form_obj})


# 增加和编辑
def add_edit_customer(request, edit_id=None):
    # 根据 id 查出所需要编辑的客户，如果不传就是 None
    obj = models.Customer.objects.filter(id=edit_id).first()
    # instance——实例
    form_obj = CustomerForm(instance=obj)
    if request.method == 'POST':
        # 将提交的数据和要修改的实例交给 form 对象
        form_obj = CustomerForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            # 新增、编辑后跳转至原页面
            # 获取到 next
            next = request.GET.get('next')
            # 如果没有就走原来的
            if next:
                return redirect(next)
            return redirect(to=reverse('customer'))
    return render(request, 'add_edit_customer.html', {'form_obj': form_obj, 'edit_id': edit_id})


# 展示客户列表
class CustomerList(View):

    def get(self, request):
        # 模糊查询
        q = self.contains_search(request, query_list=['qq', 'name', 'last_consult_date'])
        # 分公户和私户
        if request.path_info == reverse('customer'):
            all_customer = Customer.objects.filter(q, consultant__isnull=True)
        else:
            all_customer = Customer.objects.filter(q, consultant=request.user)
        # 如果长度为 0 是切不出来的
        if all_customer.count() == 0:
            return render(request, 'customer_list.html', )

        p = Pagination(request, all_count=all_customer.count())

        return render(
            request, 'customer_list.html', {
                'all_customer': all_customer[p.start:p.end],
                'pagination': p.show_li,
                'next_urlencode': self.next_urlencode(),
            })

    def post(self, request):
        # 处理 post 提交的 action
        action = request.POST.get('action')
        # 没有这个方法就是非法操作
        if not hasattr(self, action):
            return HttpResponse('非法操作')
        # 执行 multi_apply()
        ret = getattr(self, action)
        ret()
        return self.get(request)

    def multi_apply(self):
        # 保持数据的完整性和一致性

        # 公户变私户
        ids = self.request.POST.getlist('id')
        # 申请数量
        apply_number = len(ids)

        # 用户总是不能超过最大设置值
        if self.request.user.customers.count() + apply_number > settings.CUSTOMER_MAX:
            return HttpResponse('超过最大值')

        # atomic——原子性
        with transaction.atomic():
            # 根据 ids 查找加锁
            obj_list = Customer.objects.filter(id__in=ids, consultant__isnull=True).select_for_update()
            # 请求人数和查找人数要相等
            if apply_number == len(obj_list):
                # 更新
                obj_list.update(consultant=self.request.user)
            else:
                return HttpResponse('用户已被占')

    def multi_pub(self):
        # 私户变公户
        ids = self.request.POST.getlist('id')
        Customer.objects.filter(id__in=ids).update(consultant=None)

    def contains_search(self, request, query_list):
        # 模糊查询
        # 如果找不到就为空
        query = request.GET.get('query', '')
        q = Q()
        # children 的关系全是 or 的关系
        q.connector = 'OR'
        # q.children——应该是个列表
        for L in query_list:
            # Q 里面是个元组
            q.children.append(Q(('{}__contains'.format(L), query)))
        return q

    def next_urlencode(self):
        # next——新增、编辑后跳转至原页面
        url = self.request.get_full_path()
        qd = QueryDict()
        qd._mutable = True
        qd['next'] = url
        return qd.urlencode()


# 展示跟记录
class ConsultRecordList(View):
    def get(self, request, customer_id):
        if customer_id == '0':
            # 所有客户
            all_consult_record = ConsultRecord.objects.filter(delete_status=False, consultant=request.user)
        else:
            # 单个客户
            all_consult_record = ConsultRecord.objects.filter(delete_status=False, customer_id=customer_id)
        return render(request, 'consult_record_list.html', {
            'all_consult_record': all_consult_record,
            'next_urlencode': self.next_urlencode(),
        })

    def next_urlencode(self):
        url = self.request.get_full_path()
        qd = QueryDict()
        qd._mutable = True
        qd['next'] = url
        return qd.urlencode()


def add_edit_consult_record(request, edit_id=None):
    # 编辑
    # 根据 id 查出所需要编辑的客户，如果不传就是 None OR 给 form 传 request.user，consultant 关联 UserProfile
    obj = ConsultRecord.objects.filter(id=edit_id).first() or ConsultRecord(consultant=request.user)
    # instance——实例
    # 如果 edit_id=None 就是新增
    form_obj = ConsultRecordForm(instance=obj)
    # 新增和编辑都是 post 请求
    if request.method == 'POST':
        form_obj = ConsultRecordForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            # 新增、编辑后跳转至原页面
            # 获取到 next
            next = request.GET.get('next')
            # 如果没有就走原来的
            if next:
                return redirect(next)
            return request(to=reverse('my_consult_record', args=(0,)))
    return render(request, 'add_edit_customer.html', {'form_obj': form_obj})


# 报名记录
class EnrollmentList(View):
    def get(self, request, customer_id):
        if customer_id == '0':
            all_record = Enrollment.objects.filter(delete_status=False, customer__consultant=request.user)
        else:
            all_record = Enrollment.objects.filter(delete_status=False, customer_id=customer_id)

        return render(request, 'enrollment_list.html', {
            'all_record': all_record,
            'next_urlencode': self.next_urlencode(),
        })

    def next_urlencode(self):
        url = self.request.get_full_path()
        qd = QueryDict()
        qd._mutable = True
        qd['next'] = url
        return qd.urlencode()


# 增加和编辑报名记录
def add_edit_enrollment(request, customer_id=None, enrollment_id=None):
    obj = Enrollment.objects.filter(id=enrollment_id).first() or Enrollment(customer_id=customer_id)
    form_obj = EnrollmentForm(instance=obj)
    if request.method == 'POST':
        form_obj = EnrollmentForm(request.POST, instance=obj)
        if form_obj.is_valid():
            enrollment_obj = form_obj.save()
            # 修改报名表的状态
            enrollment_obj.customer.status = 'signed'
            enrollment_obj.customer.save()
            next = request.GET.get('next')
            if next:
                return redirect(to=next)
            else:
                return redirect(to=reverse('my_customer'))
    return render(request, 'add_edit_enrollment.html', {'form_obj': form_obj, 'enrollment_id': enrollment_id})


# 展示班级
class ClassList_(View):
    def get(self, request):
        # 模糊搜索
        q = self.contains_search(request, query_list=['course', 'semester'])
        all_class = models.ClassList.objects.filter(q)
        # 分页需求
        p = Pagination(request, all_class.count(), )

        return render(request, 'class_list.html', {
            'all_class': all_class[p.start:p.end],
            'pagination': p.show_li,
            'next_urlencode': self.next_urlencode(),
        })

    def contains_search(self, request, query_list):
        # 模糊查询
        # 如果找不到就为空
        query = request.GET.get('query', '')
        q = Q()
        # children 的关系全是 or 的关系
        q.connector = 'OR'
        # q.children——应该是个列表
        for L in query_list:
            # Q 里面是个元组
            q.children.append(Q(('{}__contains'.format(L), query)))
        return q

    def next_urlencode(self):
        url = self.request.get_full_path()
        qd = QueryDict()
        qd._mutable = True
        qd['next'] = url
        return qd.urlencode()


# 添加和编辑班级
def add_edit_class(request, edit_id=None):
    obj = ClassList.objects.filter(id=edit_id).first()
    form_obj = ClassForm(instance=obj)
    if request.method == 'POST':
        form_obj = ClassForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            next = request.GET.get('next')
            if next:
                return redirect(to=next)
            else:
                return redirect(to=reverse('class'))

    return render(request, 'add_edit_class.html', {
        'form_obj': form_obj,
        'edit_id': edit_id,
    })


class CourseRecordList(View):
    def get(self, request, class_id=None):
        # 模糊搜索
        q = self.contains_search(request, query_list=[])
        all_course_record = CourseRecord.objects.filter(q, re_class=class_id)
        # 分页需求
        if all_course_record.count() == 0:
            return render(request, 'course_record_list.html', {'class_id': class_id, })
        p = Pagination(request, all_course_record.count(), )
        return render(request, 'course_record_list.html', {
            'all_course_record': all_course_record[p.start:p.end],
            'pagination': p.show_li,
            'next_urlencode': self.next_urlencode(),
            'class_id': class_id,
        })

    def post(self, request, class_id):
        action = request.POST.get('action')
        if not hasattr(self, action):
            return HttpResponse('非法操作')
        ret = getattr(self, action)()
        if ret:
            return ret
        return self.get(request, class_id)

    def contains_search(self, request, query_list):
        # 模糊查询
        # 如果找不到就为空
        query = request.GET.get('query', '')
        q = Q()
        # children 的关系全是 or 的关系
        q.connector = 'OR'
        # q.children——应该是个列表
        for L in query_list:
            # Q 里面是个元组
            q.children.append(Q(('{}__contains'.format(L), query)))
        return q

    def next_urlencode(self):
        url = self.request.get_full_path()
        qd = QueryDict()
        qd._mutable = True
        qd['next'] = url
        return qd.urlencode()

    def multi_init(self):
        # 根据当前提交的课程 id 批量初始化学生记录
        course_ids = self.request.POST.getlist('id')
        # 根据课程 id 查找课程
        course_obj_list = CourseRecord.objects.filter(id__in=course_ids)
        for course_obj in course_obj_list:
            # 查询当前课程记录代表的班级学生
            all_students = course_obj.re_class.customer_set.filter(status='studying')
            # 找到学生创建学习记录
            student_list = []
            for student in all_students:
                student_list.append(StudyRecord.objects.create(course_record=course_obj, student=student))
            # 批量创建——走一条 sql 语句
            StudyRecord.objects.bulk_create(student_list)


def add_edit_course_record(request, class_id=None, edit_id=None):
    # 后面的不是 object
    obj = CourseRecord.objects.filter(id=edit_id).first() or CourseRecord(re_class_id=class_id, teacher=request.user)
    form_obj = CourseRecordForm(instance=obj)
    if request.method == 'POST':
        form_obj = CourseRecordForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            next = request.GET.get('next')
            if next:
                return redirect(to=next)
            else:
                return redirect(to=reverse('course_record', args=(class_id,)))

    return render(request, 'add_edit_course_record.html', {
        'form_obj': form_obj,
        'edit_id': edit_id,
    })


# 展示学习记录
from django.forms import modelformset_factory


def study_record(request, course_id):
    #
    ModelFormSet = modelformset_factory(StudyRecord, StudyRecordForm, extra=0)
    #
    queryset = StudyRecord.objects.filter(course_record_id=course_id)
    # print(queryset)
    # 实例化
    mfs = ModelFormSet(queryset=queryset)
    if request.method == 'POST':
        mfs = ModelFormSet(request.POST)
        if mfs.is_valid():
            mfs.save()
    return render(request, 'study_record_list.html', {'mfs': mfs})
