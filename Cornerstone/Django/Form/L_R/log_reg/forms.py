# -*- coding: utf-8 -*-
# @Time : 2019/6/20 16:30
# @Author : Quantum-Ran
# @Email : ai.ei.ui@live.cn
# @File : forms.py
# @Software: PyCharm
from django import forms
# widgets——插件
from django.forms import widgets
from .models import *
# from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re


# 自定义验证函数
# def check_phone(value):
#     if not re.compile(r'^1[3-9]\d{9}$').match(value):
#         raise ValidationError('手机格式不正确')


# 定义 form
class RegForm(forms.Form):
    # 自动刷新
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.fields['hobby'].choices)

    # label——命名
    username = forms.CharField(
        label='用户名',
        min_length=6,
        # initial——初始值
        initial='szl',
        # error_messages——重制错误信息
        error_messages={
            'min_length': '密码最小六位',
            'required': '不能为空'
        })
    password = forms.CharField(
        label='密码',
        min_length=6,
        # widgets.PasswordInput()——密文
        widget=widgets.PasswordInput(),
        error_messages={
            'min_length': '密码最小六位',
            'required': '不能为空',
        })
    re_password = forms.CharField(
        label='确认密码',
        min_length=6,
        # widgets.PasswordInput()——密文
        widget=widgets.PasswordInput(),
        error_messages={
            'min_length': '密码最小六位',
            'required': '不能为空',
        })
    gender = forms.ChoiceField(
        label='性别',
        choices=((1, '男'), (2, '女'), (3, '不详')),
        widget=widgets.RadioSelect(),
        error_messages={
            'required': '不能为空',
        })
    hobby = forms.ChoiceField(
        label='爱好',
        # choices=((1, '篮球'), (2, '足球')),
        choices=Hobby.objects.all().values_list('id', 'name'),
        widget=widgets.CheckboxSelectMultiple(),
    )
    phone = forms.CharField(
        label='手机号',
        # validators——校验器 可以放多个
        # validators=[
        #     # RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误')
        #     # 自定义的
        #     check_phone,
        # ]
    )

    # 钩子函数
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if re.compile(r'^1[3-9]\d{9}$').match(phone):
            return phone
        else:
            raise ValidationError('手机格式不正确')

    # def clean_re_password(self):
    #     pwd = self.cleaned_data.get('password')
    #     re_pwd = self.cleaned_data.get('re_password')
    #     if pwd == re_pwd:
    #         return re_pwd
    #     else:
    #         raise ValidationError('密码不一致')

    # 全局钩子——所有局部钩子都校验完再做校验
    def clean(self):
        pwd = self.cleaned_data.get('password')
        re_pwd = self.cleaned_data.get('re_password')
        if pwd == re_pwd:
            return self.cleaned_data
        # 加入错误
        self.add_error('re_password', '两次密码不一致')
        raise ValidationError('密码不一致')
