# Get

## status_code——状态码

![1555124466012](Get.assets/1555124466012.png)

![1555124505296](Get.assets/1555124505296.png)

<table>
    <tr>
    	<td>1**</td>
        <td>信息，服务器收到请求，需要请求者继续执行操作</td>
    </tr>
    <tr>
    	<td>2**</td>
        <td>成功，操作被成功接收并处理</td>
    </tr>
    <tr>
    	<td>3**</td>
        <td>重定向，需要进一步的操作以完成请求</td>
    </tr>
    <tr>
    	<td>4**</td>
        <td>客户端错误，请求包含语法错误或无法完成请求</td>
    </tr>
    <tr>
    	<td>5**</td>
        <td>服务器错误，服务器在处理请求的过程中发生了错误</td>
    </tr>
</table>

## 响应头

![1555124963536](Get.assets/1555124963536.png)

## 请求头

![1555125145967](Get.assets/1555125145967.png)

### 由于 默认的 User-Agent 和普通的浏览器不一样，所以要模拟一个 User-Agent 的请求头

![1555125344603](Get.assets/1555125344603.png)

![1555125733068](Get.assets/1555125733068.png)

### 带参数请求

![1555126562862](Get.assets/1555126562862.png)



![1555126534351](Get.assets/1555126534351.png)

## response.text diff response.content.decode()

<table>
    <tr>
    	<td colspan='2'>都是为了获取响应的html页面</td>
    </tr>
    <tr>
    	<td>response.text</td>
        <td>type: str</td>
    </tr>
    <tr>
    	<td>response.content.decode('utf8')</td>
        <td>type: bytes</td>
    </tr>
</table>
## Proxies

`http://www.httpbin.org/ip`

![1557570831572](Get.assets/1557570831572.png)

![1557570847626](Get.assets/1557570847626.png)

# cookiejar 和 dict

## cookiejar → dict

![1555817316311](Get.assets/1555817316311.png)

## dict → cookiejar

![1555817428657](Get.assets/1555817428657.png)

# 请求 SSL 证书错误验证

![1555817685527](Get.assets/1555817685527.png)

![1555818187868](Get.assets/1555818187868.png)

# 设置超时参数

![1555818134270](Get.assets/1555818134270.png)


