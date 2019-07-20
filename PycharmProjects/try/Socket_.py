# -*- coding: utf-8 -*-
# @Time : 2019/6/9 10:30
# @Author : Ran
# @Email : ai.ei.ui@live.cn
# @File : Socket_.py
# @Software: PyCharm
import socket

ss = socket.socket()
# 绑定地址
ss.bind(('127.0.0.1', 8888))
# 开始TCP监听
ss.listen(5)
while 1:
    # 被动接受TCP客户端连接（阻塞式）等待连接的到来
    connect, address = ss.accept()
    # 接收TCP数据，数据以字符串形式返回
    # 请求头 和 请求体
    data = connect.recv(8096)
    # 请求头，请求体
    # data 是 bytes 类型需要解码
    headers, body = str(data, encoding='utf8').split('\r\n\r\n')
    temp_list = headers.split('\r\n')
    # 请求方式,url,protocal
    method, url, protocal = temp_list[0].split()
    # 发送 TCP 数据
    if url == '/':
        connect.send(b'200')
    else:
        connect.send(b'404')
    # # 响应头
    # connect.send(b'HTTP/1.1 200 OK\r\n\r\n')
    # # 响应体
    # connect.send(b'')
    # 关闭
    connect.close()
