# Downloader Middlewares

下载器中间件是介于Scrapy的 request/response 处理的钩子框架。 是用于全局修改 Scrapy request 和 response 的一个轻量、底层的系统。

![request通过下载中间件](Downloader_Middlewares.assets/request通过下载中间件.svg)

- 激活——不覆盖，有优先级。

![1563430761191](Downloader_Middlewares.assets/1563430761191.png)

- `process_request(request, spider)`——请求

![1563430980067](Downloader_Middlewares.assets/1563430980067.png)

- `process_response(request, response, spider)`——响应

![1563432044685](Downloader_Middlewares.assets/1563432044685.png)

- `process_exception(request, exception, spider)`——异常

![1563432117989](Downloader_Middlewares.assets/1563432117989.png)

<ol>
	<li><a href='随机请求头'>随机请求头</a></li>
    <li><a href='IP代理池'>IP代理池</a></li>
</ol>

