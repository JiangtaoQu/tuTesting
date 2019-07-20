# -*- coding: utf-8 -*-
# @Time : 2019/6/19 16:22
# @Author : Quantum-Ran
# @Email : ai.ei.ui@live.cn
# @File : forms.py
# @Software: PyCharm
from django import forms
from app import models
from django.core.exceptions import ValidationError


class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for filed in self.fields.values():
            filed.widget.attrs.update({'class': 'form-control'})


# 注册
# ModelForm —— 和 model 类似有 class Meta
class RegForm(BaseForm):
    # 没有字段可以自己加
    re_password = forms.CharField(
        label='确认密码',
        widget=forms.widgets.PasswordInput(),
    )
    password = forms.CharField(
        label='密码',
        widget=forms.widgets.PasswordInput(),
        min_length=6,
    )

    class Meta:
        model = models.UserProfile
        # '__all__'——指定所有
        fields = ['username', 'password', 're_password', 'name', 'department']
        # exclude = []——排除字段
        # 这里是复数 widgets
        widgets = {
            'username': forms.widgets.EmailInput(
                attrs={
                    'class': 'form-control'}), }
        labels = {
            'username': '用户名',
            'name': '名称',
            'department': '部门',
        }
        error_messages = {
            'min_length': '最小长度为6',
            'required': '密码不能为空',
        }

    def clean(self):
        pwd = self.cleaned_data.get('password')
        re_pwd = self.cleaned_data.get('re_password')
        if pwd == re_pwd:
            return self.cleaned_data
        self.add_error('re_password', '两次密码不一致')
        raise ValidationError('两次密码不一致')


# 客户 form
class CustomerForm(BaseForm):
    class Meta:
        model = models.Customer
        fields = '__all__'
        widgets = {
            'course': forms.widgets.SelectMultiple,
        }


# 跟进记录
class ConsultRecordForm(BaseForm):
    # 1.Meta 先执行
    class Meta:
        model = models.ConsultRecord
        # fields = '__all__'
        exclude = ['delete_status', ]

    # 增加跟进客户时，只显示自己的客户
    def __init__(self, *args, **kwargs):
        super(ConsultRecordForm, self).__init__(*args, **kwargs)
        # 2.父类方法都执行完再执行
        # 需要标识自己的 request.user
        # 限制客户是当前销售所有的客户
        self.fields['customer'].widget.choices = [(i.id, i) for i in self.instance.consultant.customers.all()]
        self.fields['customer'].widget.choices.insert(0, ('', '----------'))
        # 限制是当前的销售
        self.fields['consultant'].widget.choices = [(self.instance.consultant.id, self.instance.consultant)]


# 报名表
class EnrollmentForm(BaseForm):
    class Meta:
        model = models.Enrollment
        exclude = ['delete_status', 'contract_approved']

    def __init__(self, *args, **kwargs):
        super(EnrollmentForm, self).__init__(*args, **kwargs)
        # 限制当前客户只能是 id 对应的客户
        self.fields['customer'].widget.choices = ((self.instance.customer_id, self.instance.customer),)
        # 限制当前可报名的班级是当前客户的意向班级
        self.fields['enrolment_class'].widget.choices = [(i.id, i) for i in self.instance.customer.class_list.all()]


# 班级表
class ClassForm(BaseForm):
    class Meta:
        model = models.ClassList
        fields = '__all__'


# 课程表
class CourseRecordForm(BaseForm):
    def __init__(self, *args, **kwargs):
        super(CourseRecordForm, self).__init__(*args, **kwargs)
        print('1' * 100, self.instance)
        # 限制当前班级只能是 id 对应的客户
        self.fields['re_class'].widget.choices = ((self.instance.re_class_id, self.instance.re_class),)
        # 限制当前的班主任是当前客户
        self.fields['teacher'].widget.choices = [(self.instance.teacher_id, self.instance.teacher)]

    class Meta:
        model = models.CourseRecord
        fields = '__all__'


# 学习记录
class StudyRecordForm(BaseForm):
    class Meta:
        model = models.StudyRecord
        fields = ['attendance', 'score', 'homework_note', 'student']
