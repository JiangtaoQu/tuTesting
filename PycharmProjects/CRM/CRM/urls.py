"""CRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', first),
    re_path('^login_/$', login),
    re_path('^register_/$', register),
    # 公户
    # re_path('^customer_list/$', customer_list, name='customer'),
    # 私户
    # re_path('^my_customer_list/$', customer_list, name='my_customer'),
    # 类方法 as_view() 只要视图继承 View 就自动出来
    # 公户
    re_path(r'^customer_list/$', CustomerList.as_view(), name='customer'),
    # 私户
    re_path(r'^my_customer_list/$', CustomerList.as_view(), name='my_customer'),
    # re_path('^user_list/$', user_list),
    # 增加客户
    # re_path('^customer/add/$', add_customer, name='add_customer'),
    # 编辑用户
    # re_path(r'^customer/edit/(\d+)/$', edit_customer, name='edit_customer'),
    # 新增和编辑客户
    re_path(r'^customer/$', add_edit_customer, name='add_customer'),
    re_path(r'^customer/(\d+)/$', add_edit_customer, name='edit_customer'),
    # 展示跟进记录
    # re_path(r'^consult_record_list/(\d+)/$', ConsultRecordList.as_view(), name='consult_recode'),
    # 我的跟进客户
    re_path(r'^my_consult_record_list/(\d+)/$', ConsultRecordList.as_view(), name='my_consult_record'),
    # 新增和编辑跟进记录
    re_path(r'^consult_record/$', add_edit_consult_record, name='add_consult_record'),
    re_path(r'^consult_record/(\d+)/$', add_edit_consult_record, name='edit_consult_record'),
    # 展示报名记录
    re_path(r'^enrollment_list/(?P<customer_id>\d+)/$', EnrollmentList.as_view(), name='enrollment'),
    # 新增和编辑报名记录
    re_path(r'^enrollment/add/(?P<customer_id>\d+)/$', add_edit_enrollment, name='add_enrollment'),
    re_path(r'^enrollment/edit/(?P<enrollment_id>\d+)/$', add_edit_enrollment, name='edit_enrollment'),
    # 展示班级列表
    re_path(r'^class_list/$', ClassList_.as_view(), name='class'),
    # 添加和编辑班级
    re_path(r'^class/add/$', add_edit_class, name='add_class'),
    re_path(r'^class/edit/(?P<edit_id>\d+)/$', add_edit_class, name='edit_class'),
    # 课程记录
    re_path(r'^course_record_list/(?P<class_id>\d+)/$', CourseRecordList.as_view(), name='course_record'),
    # 增加和编辑课程记录
    re_path(r'^course_record/add/(?P<class_id>\d+)/$', add_edit_course_record, name='add_course_record'),
    re_path(r'^course_record/edit/(?P<edit_id>\d+)/$', add_edit_course_record, name='edit_course_record'),
    # 展示学习记录
    re_path(r'^study_record_list/(?P<course_id>\d+)/$', study_record, name='study_record'),
    #
]
