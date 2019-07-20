from django.shortcuts import render, HttpResponse
from log_reg.forms import *


# Create your views here.
def first(request):
    return render(request, 'first.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    # 1.实例化 form
    form_obj = RegForm()
    # 3.提取 post 数据
    if request.method == 'POST':
        # 4.把 request.POST 的数据放进 form 去做校验
        form_obj = RegForm(request.POST)
        # 5.如果 form_obj 是通过校验的
        if form_obj.is_valid():
            # 只有经过校验后才会有 cleaned_data——干净的数据
            print(form_obj.cleaned_data)
            return HttpResponse('成功')

    # 2.把对象交给模板
    return render(request, 'register.html', {'form_obj': form_obj})
