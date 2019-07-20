from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin, AbstractUser, BaseUserManager, \
    _user_has_perm, _user_has_module_perms
from django.utils import timezone
from multiselectfield import MultiSelectField
from django.shortcuts import reverse
from django.utils.safestring import mark_safe

from django.contrib import auth
from django.core.exceptions import PermissionDenied
from django.utils.translation import ugettext_lazy as _

# Create your models here.
gender_type = ((1, '男'), (2, '女'))
source_type = (('qq', 'qq群'),
               ('referral', '内部转介绍'),
               ('website', '官方网站'),
               ('baidu_ads', '百度推广'),
               ('office_direct', '直接上门'),
               ('WoM', '口碑'),
               ('public_class', '公开课'),
               ('other', '其他'),)
course_choices = (('Linux', 'Linux中高级'), ('PythonFullStack', 'Python高级全栈开发'))
class_type_choices = (('fulltime', '脱产班'),
                      ('online', '网络班'),
                      ('weekend', '周末班'),)
enroll_status_choices = (('signed', '已报名'),
                         ('unregistered', '未报名'),
                         ('studying', '学习中'),
                         ('paid_in_full', '学费已交付'),)

seek_status_choices = (('A', '近期无报名计划'), ('B', '1个月内报名'), ('C', '2周内报名'),
                       ('D', '1周内报名'), ('E', '定金'), ('F', '到班'), ('G', '全款'), ('H', '无效'))

pay_type_choices = (('deposit', '订金/报名费'),
                    ('tuition', '学费'),
                    ('transfer', '转班'),
                    ('dropout', '退学'),
                    ('refund', '退款'),)

status_choices = ((1, '未审核'),
                  (2, '已审核'),)

attendance_choices = (('checked', "已签到"),
                      ('vacate', "请假"),
                      ('late', "迟到"),
                      ('absence', "缺勤"),
                      ('leave_early', "早退"),)

score_choices = ((100, 'A+'),
                 (90, 'A'),
                 (85, 'B+'),
                 (80, 'B'),
                 (70, 'B-'),
                 (60, 'C+'),
                 (50, 'C'),
                 (40, 'C-'),
                 (0, ' D'),
                 (-1, 'N/A'),
                 (-100, 'COPY'),
                 (-1000, 'FAIL'),)


class Campuses(models.Model):
    name = models.CharField(max_length=64, verbose_name='校区')
    address = models.CharField(
        max_length=512,
        verbose_name='详细地址',
        blank=True,
        null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '校区表'
        verbose_name_plural = verbose_name


class ClassList(models.Model):
    course = models.CharField(
        max_length=64,
        choices=course_choices,
        verbose_name='课程名称')
    semester = models.IntegerField(verbose_name='学期')
    campuses = models.ForeignKey(
        to='Campuses',
        on_delete=models.CASCADE,
        verbose_name='校区')
    price = models.IntegerField(verbose_name='学费')
    memo = models.CharField(
        max_length=255,
        verbose_name='说明',
        blank=True,
        null=True)
    start_date = models.DateField(verbose_name='开班日期')
    graduate_date = models.DateField(verbose_name='结业日期')
    contract = models.ForeignKey(
        to='ContractTemplate',
        on_delete=models.CASCADE,
        verbose_name='选择合同模板',
        blank=True,
        null=True)
    teachers = models.ManyToManyField(to='UserProfile', verbose_name='老师')
    class_type = models.CharField(
        max_length=64,
        choices=class_type_choices,
        verbose_name='班级类型',
        blank=True,
        null=True)

    def __str__(self):
        # get_course_display()——获取 choices 对应的汉字
        return '{}{}({})'.format(self.get_course_display(),
                                 self.semester,
                                 self.campuses, )

    def show_teachers(self):
        return '|'.join([str(i) for i in self.teachers.all()])

    class Meta:
        # 联合唯一
        unique_together = ('course', 'semester', 'campuses')
        verbose_name = '课程表'
        verbose_name_plural = verbose_name


class Customer(models.Model):
    qq = models.CharField(
        max_length=64,
        verbose_name='QQ',
        unique=True,
        help_text='QQ号码必须唯一')
    # blank=True—— admin 可以为空，null=True—— db 可以为空
    name = models.CharField(
        max_length=32,
        verbose_name='姓名',
        blank=True,
        null=True,
        help_text='真实姓名')
    gender = models.IntegerField(
        choices=gender_type,
        verbose_name='性别',
        default=1,
        blank=True,
        null=True,
        help_text='可以隐私保密')
    birthday = models.DateField(
        default=None,
        blank=True,
        null=True,
        verbose_name='生日',
        help_text='格式YYYY-mm-dd')
    phone_number = models.CharField(
        max_length=11,
        verbose_name='手机号',
        blank=True,
        null=True)
    source = models.CharField(
        max_length=64,
        verbose_name='客户来源',
        choices=source_type,
        default='qq')
    # 自关联
    introduce_from = models.ForeignKey(
        to='self',
        on_delete=models.CASCADE,
        verbose_name='转介绍自学员',
        blank=True,
        null=True)
    course = MultiSelectField(verbose_name='课程咨询', choices=course_choices)
    class_type = models.CharField(
        max_length=64,
        verbose_name='班级类型',
        choices=class_type_choices,
        default='fulltime')
    customer_note = models.TextField(
        verbose_name='客户备注', blank=True, null=True)
    status = models.CharField(
        max_length=64,
        verbose_name='状态',
        choices=enroll_status_choices,
        default='unregistered',
        help_text='选择客户此时的状态')
    network_consult_note = models.TextField(
        verbose_name='网络咨询师咨询内容', blank=True, null=True)
    date = models.DateTimeField(verbose_name='咨询日期', auto_now_add=True)
    last_consult_date = models.DateField(
        verbose_name='最后跟进日期', auto_now_add=True)
    next_date = models.DateField(
        verbose_name='预计再次跟进时间',
        blank=True,
        null=True)
    network_consultant = models.ForeignKey(
        to='UserProfile',
        on_delete=models.CASCADE,
        verbose_name='咨询师',
        blank=True,
        null=True,
        related_name='network_consultant')
    consultant = models.ForeignKey(
        to='UserProfile',
        on_delete=models.CASCADE,
        verbose_name='销售',
        related_name='customers',
        blank=True,
        null=True,
    )
    #                     blank=True——admin 可以为空，数据库层面不能为空，校验需要这个字段
    class_list = models.ManyToManyField(to='ClassList', verbose_name='已报班级', blank=True)

    def __str__(self):
        return self.qq

    def show_status(self):
        color_dict = {
            'signed': 'pink',
            'unregistered': 'red',
            'studying': 'green',
            'paid_in_full': 'blue',
        }
        return '<span style="background-color: {};color: white;padding: 4px">{}<span>'.format(
            color_dict.get(self.status), self.get_status_display())

    def show_classes(self):
        return ' | '.join([str(i) for i in self.class_list.all()])

    # 根据状态的不同报名记录可删除可添加
    def enrollment_link(self):
        if not self.enrollment_set.exists():
            return '<a href="{}">添加</a>'.format(reverse('add_enrollment', args=(self.id,)))
        else:
            return '<a href="{}">添加</a>|<a href="{}">查看</a>'.format(
                reverse('add_enrollment', args=(self.id,)),
                reverse('enrollment', args=(self.id,)),
            )

    class Meta:
        verbose_name = '客户表'
        verbose_name_plural = verbose_name


class ContractTemplate(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name='合同名称')
    content = models.TextField(verbose_name='合同内容')
    date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = '合同模板'
        verbose_name_plural = verbose_name


class Department(models.Model):
    name = models.CharField(max_length=32, verbose_name='部门名称')
    count = models.IntegerField(default=0, verbose_name='人数')

    class Meta:
        verbose_name = '部门表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 相比源码的 usermanager 去除了 email 字段
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        username = self.normalize_email(username)
        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    # unique=True——唯一
    username = models.EmailField(max_length=255, unique=True, )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    # objects——管理工具
    objects = UserManager()

    EMAIL_FIELD = 'email'
    # USERNAME_FIELD——登录用户名
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

    class Meta:
        verbose_name = '账户信息'
        verbose_name_plural = "账户信息"

    def get_full_name(self):
        # The user is identified by their email address
        return self.name

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def __str__(self):  # __unicode__ on Python 2
        return self.username

    def has_perm(self, perm, obj=None):
        #     "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always

        if self.is_active and self.is_superuser:
            return True
        return _user_has_perm(self, perm, obj)

    def has_perms(self, perm_list, obj=None):
        #     "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        for perm in perm_list:
            if not self.has_perm(perm, obj):
                return False
        return True

    def has_module_perms(self, app_label):
        #     "Does the user have permissions to view the app `app_label`?"
        #     Simplest possible answer: Yes, always
        if self.is_active and self.is_superuser:
            return True

        return _user_has_module_perms(self, app_label)

    # 自己需要的
    is_admin = models.BooleanField(default=True)
    name = models.CharField(verbose_name='名称', max_length=32)
    department = models.ForeignKey(
        to='Department',
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True)
    mobile = models.CharField(
        max_length=11,
        verbose_name='手机',
        default=None,
        blank=True,
        null=True)


class ConsultRecord(models.Model):
    customer = models.ForeignKey(
        to='Customer',
        on_delete=models.CASCADE,
        verbose_name='所咨询客户')
    note = models.TextField(verbose_name='跟进内容')
    status = models.CharField(
        max_length=8,
        choices=seek_status_choices,
        verbose_name='跟进状态',
        help_text='客户当前状态')
    consultant = models.ForeignKey(
        to='UserProfile',
        on_delete=models.CASCADE,
        verbose_name='跟进人',
        related_name='records',
    )
    date = models.DateTimeField(auto_now_add=True, verbose_name='跟进日期')
    delete_status = models.BooleanField(verbose_name='删除状态', default=False)

    class Meta:
        verbose_name = '跟进记录表'
        verbose_name_plural = verbose_name

    def show_status(self):
        color_dict = {
            'signed': 'pink',
            'unregistered': 'red',
            'studying': 'green',
            'paid_in_full': 'blue',
        }
        return '<span style="background-color: {};color: white;padding: 4px">{}<span>'.format(
            color_dict.get(self.status), self.get_status_display())


class Enrollment(models.Model):
    why_us = models.TextField(
        verbose_name='为什么报名',
        default=None,
        blank=True,
        null=True)
    your_expectation = models.TextField(
        verbose_name='学完想达到的具体期望', blank=True, null=True)
    contract_agreed = models.BooleanField(
        verbose_name='我已认真阅读完培训协议并同意全部协议内容', default=False)
    contract_approved = models.BooleanField(
        verbose_name='审批通过',
        help_text="在审阅完学员的资料无误后勾选此项,合同即生效",
        default=False)
    enrolled_date = models.DateTimeField(
        auto_now_add=True, verbose_name="报名日期")
    memo = models.TextField(verbose_name='备注', blank=True, null=True)
    delete_status = models.BooleanField(verbose_name='删除状态', default=False)
    customer = models.ForeignKey(
        to='Customer',
        on_delete=models.CASCADE,
        verbose_name='客户名称')
    school = models.ForeignKey(
        to='Campuses',
        on_delete=models.CASCADE,
        verbose_name='学校')
    enrolment_class = models.ForeignKey(
        to='ClassList',
        on_delete=models.CASCADE,
        verbose_name='所报班级')

    class Meta:
        verbose_name = '报名表'
        verbose_name_plural = verbose_name
        unique_together = ('enrolment_class', 'customer')


class PaymentRecord(models.Model):
    pay_type = models.CharField(
        max_length=64,
        verbose_name="费用类型",
        choices=pay_type_choices,
        default="deposit")
    paid_fee = models.IntegerField(verbose_name="费用数额", default=0)
    note = models.TextField(verbose_name="备注", blank=True, null=True)
    date = models.DateTimeField(verbose_name="交款日期", auto_now_add=True)
    course = models.CharField(
        verbose_name="课程名",
        choices=course_choices,
        max_length=64,
        blank=True,
        null=True,
        default='N/A')
    class_type = models.CharField(
        verbose_name="班级类型",
        choices=class_type_choices,
        max_length=64,
        blank=True,
        null=True,
        default='N/A')
    enrolment_class = models.ForeignKey(
        to='ClassList',
        on_delete=models.CASCADE,
        verbose_name='所报班级',
        blank=True,
        null=True)
    customer = models.ForeignKey(
        to='Customer',
        on_delete=models.CASCADE,
        verbose_name="客户")
    consultant = models.ForeignKey(
        to='UserProfile',
        on_delete=models.CASCADE,
        verbose_name="销售")
    delete_status = models.BooleanField(verbose_name='删除状态', default=False)
    status = models.IntegerField(
        choices=status_choices,
        verbose_name='审核',
        default=1)
    confirm_date = models.DateTimeField(
        verbose_name="确认日期", null=True, blank=True)
    confirm_user = models.ForeignKey(
        to='UserProfile',
        on_delete=models.CASCADE,
        verbose_name="确认人",
        related_name='confirms',
        null=True,
        blank=True)

    class Meta:
        verbose_name = '缴费记录表'
        verbose_name_plural = verbose_name


class CourseRecord(models.Model):
    day_num = models.IntegerField(
        verbose_name="节次",
        help_text="此处填写第几节课或第几天课程...,必须为数字")
    date = models.DateField(auto_now_add=True, verbose_name="上课日期")
    course_title = models.CharField(
        max_length=64,
        verbose_name='本节课程标题',
        blank=True,
        null=True)
    course_memo = models.TextField(
        verbose_name='本节课程内容', blank=True, null=True)
    has_homework = models.BooleanField(default=True, verbose_name="本节有作业")
    homework_title = models.CharField(
        max_length=64,
        verbose_name='本节作业标题',
        blank=True,
        null=True)
    homework_memo = models.TextField(
        max_length=500,
        verbose_name='作业描述',
        blank=True,
        null=True)
    scoring_point = models.TextField(
        max_length=300,
        verbose_name='得分点',
        blank=True,
        null=True)
    re_class = models.ForeignKey(
        to='ClassList',
        on_delete=models.CASCADE,
        verbose_name="班级")
    teacher = models.ForeignKey(
        to='UserProfile',
        on_delete=models.CASCADE,
        verbose_name="班主任")

    def __str__(self):
        return '{}({})'.format(self.re_class, self.day_num)

    class Meta:
        verbose_name = '课程记录表'
        verbose_name_plural = verbose_name
        unique_together = ('re_class', 'day_num')


class StudyRecord(models.Model):
    attendance = models.CharField(
        max_length=64,
        verbose_name="考勤",
        choices=attendance_choices,
        default="checked",
    )
    score = models.IntegerField(
        verbose_name="本节成绩",
        choices=score_choices,
        default=-1)
    homework_note = models.CharField(
        max_length=255,
        verbose_name='作业批语',
        blank=True,
        null=True)
    date = models.DateTimeField(auto_now_add=True)
    note = models.CharField(
        max_length=255,
        verbose_name="备注",
        blank=True,
        null=True)
    homework = models.FileField(
        verbose_name='作业文件',
        blank=True,
        null=True,
        default=None)
    course_record = models.ForeignKey(
        to='CourseRecord',
        on_delete=models.CASCADE,
        verbose_name="某节课程")
    student = models.ForeignKey(
        to='Customer',
        on_delete=models.CASCADE,
        verbose_name="学员")

    class Meta:
        verbose_name = '学习记录'
        verbose_name_plural = verbose_name
        unique_together = ('course_record', 'student')
