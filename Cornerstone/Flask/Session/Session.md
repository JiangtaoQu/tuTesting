# Session

1. 当请求刚到来：flask 读取 cookie 中 session 对应的值：`eyJrMiI6vyIjoib26ndu2lcj1c22xkym95`，将该值解密并反序列化成字典，放入内存，以便视图函数使用。

2. 当请求结束时， flask 会读取内存中的字典的值，进行序列化+加密，写入到用户 cookie 中。

