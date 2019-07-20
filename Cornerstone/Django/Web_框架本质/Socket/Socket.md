# Socket

- 浏览器——socket client

- 网站——socket server

## 服务端

- `socket.socket()`——创建实例

![1560049756289](Socket.assets/1560049756289.png)

- `socket.bind((【host,port】))`——绑定地址（host,port）到套接字， 在 AF_INET 下，元组（host,port）的形式表示地址。

![1560045439601](Socket.assets/1560045439601.png)

- `socket.listen(【backlog】)`——开始TCP监听。backlog 指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了。

![1560045579447](Socket.assets/1560045579447.png)

- `socket.accept()`——被动接受TCP客户端连接（阻塞式）等待连接的到来

![1560048074808](Socket.assets/1560048074808.png)

- `connect.recv(【bufsize】)`——接收 TCP 数据，数据以字符串形式返回，bufsize 指定要接收的最大数据量。flag 提供有关消息的其他信息，通常可以忽略。

![1560045949045](Socket.assets/1560045949045.png)

- GET 请求头

![1560049184495](Socket.assets/1560049184495.png)

- POST 请求头

![1560049330548](Socket.assets/1560049330548.png)

- 根据 url 去往不同的网页

![1560052666983](Socket.assets/1560052666983.png)

- 响应头

![1560049467561](Socket.assets/1560049467561.png)

- 响应体——用户看到的数据

- `connect.send(【data】)`——发送 TCP 数据，将 string 中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于 string 的字节大小。

![1560046139336](Socket.assets/1560046139336.png)

## 客户端


