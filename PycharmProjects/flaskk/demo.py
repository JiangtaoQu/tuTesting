# -*- coding: utf-8 -*-
# @Time : 2019/6/11 17:24
# @Author : Quantum-Ran
# @Email : ai.ei.ui@live.cn
# @File : demo.py
# @Software: PyCharm
from flask import Flask, render_template, request, redirect, session, url_for, jsonify, make_response, Markup, flash, \
    get_flashed_messages
import functools

# 实例化
app = Flask(__name__)
# flask 配置文件
# print(app.config)
# 更改配置文件
app.config.from_object('settings.DevelopmentConfig')

# 数据库存的数据
STUDENT_dict = {
    1: {'name': '宋子良', 'age': 10, 'gender': '男'},
    2: {'name': '睡着了', 'age': 12, 'gender': '女'},
    3: {'name': '甚至连', 'age': 9, 'gender': '男'},
}


# 验证的装饰器：单一加装
def auth(func):
    # functools.wraps(func)——把传入的函数，信息还原
    # @functools.wraps(func)
    def inner(*args, **kwargs):
        if not session.get('user'):
            return redirect(url_for('login'))
        ret = func(*args, **kwargs)
        return ret

    return inner


# before_request——每一个请求之前先执行
# 相当于验证中间键，批量处理
# @app.before_request
# def global_auth():
#     if request.path == '/login':
#         # 如果有返回值就不走视图了
#         return None
#     if session.get('user'):
#         return None
#     return redirect('/login')


# after_request——相比于 before_request 必须有参数和返回值。
@app.after_request
def aft_request(response):
    print('after')
    return response


# before_first_request——启动起来第一次且仅第一次执行。
@app.before_first_request
def bfr_f_request():
    print('before')


# errorhandler——定制报错
@app.errorhandler(404)
def not_found(arg):
    return arg


# endpoint——反向生成 url；url_for(【endpoint, **values】)
# <int:nid>——<类型:id> 动态的路由
@app.route('/index', methods=['GET', 'POST'])
# @auth
def index():
    return render_template('index.html', **{'stu_dict': STUDENT_dict})


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    del STUDENT_dict[id]
    return redirect(url_for('index'))


@app.route('/detail/<int:id>', methods=['GET', 'POST'])
def detail(id):
    info = STUDENT_dict[id]
    return render_template('detail.html', **{'info': info})


@app.route('/')
def first():
    return render_template('first.html')


# 用户登录           默认只支持 GET 请求，但可以改
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # 要返回页面
        return render_template('login.html')
    # request.args——request.get
    # request.form——request.post
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    if user == 'szl' and pwd == '666':
        session['user'] = user
        return redirect('/index')
    return render_template('login.html', **{'error': '用户名或密码错误'})


# template_global()——将函数自动传入模板
@app.template_global()
def func(a, b, c):
    return a + b + c


# template_filter()——可以跟在 if 后面
@app.template_filter()
def func1(a, b, c):
    return a * b - c


@app.route('/tpl')
def tpl():
    context = {
        'user': ['宋子良', '章士通', '王孙旧'],
        # Markup——使前端信任
        'txt': Markup('<input type="text">'),
        'num1': 1,
        'num2': 2,
    }
    return render_template('tpl.html', **context)


# flash——闪现
@app.route('/page1')
def page1():
    flash('lala')


# get_flashed_messages——获取闪现
@app.route('/page2')
def page2():
    get_flashed_messages()


if __name__ == '__main__':
    # 启动 socket
    app.run()
