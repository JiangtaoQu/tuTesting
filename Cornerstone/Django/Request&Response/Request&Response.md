# Request

![1560829163025](Request&Response.assets/1560829163025.png)

- path_info——返回用户访问 **url**，不包括域名

![1560829918536](Request&Response.assets/1560829918536.png)

![1560829946093](Request&Response.assets/1560829946093.png)

-  method——请求中使用的 HTTP **方法**的字符串表示，**全大写**表示

![1560829518392](Request&Response.assets/1560829518392.png)

![1560829503653](Request&Response.assets/1560829503653.png)

- GET——包含所有 HTTP **GET** 参数的类字典对象

`url = 127.0.0.1:8000/edit_book/?id=1&name=yimi`

![1560830248938](Request&Response.assets/1560830248938.png)

![1560830236409](Request&Response.assets/1560830236409.png)

- POST——包含所有 HTTP **POST** 参数的类字典对象

- 请求数据

<table>
    <tr>
    	<td></td>
        <td>request.GET</td>
        <td>request.POST</td>
    </tr>
    <tr>
    	<td>GET 请求</td>
        <td>有</td>
        <td>可能有</td>
    </tr>
    <tr>
    	<td>POST 请求</td>
        <td>无</td>
        <td>有</td>
    </tr>
</table>

- body——请求体，**byte** 类型 request.POST 的数据就是从 body 里面提取到的

![1560829453830](Request&Response.assets/1560829453830.png)

![1560829461436](Request&Response.assets/1560829461436.png)

- FILES——上传文件

![1560829676322](Request&Response.assets/1560829676322.png)

![1560829578696](Request&Response.assets/1560829578696.png)

- scheme——返回是什么网络协议 *http;https*

scheme$_{skēm}$—方案

![1560829800094](Request&Response.assets/1560829800094.png)

![1560829776319](Request&Response.assets/1560829776319.png)



# Response

- HttpResponse——返回字符串内容

- render——返回一个html页面

![1560838153828](Request&Response.assets/1560838153828.png)

- redirect——返回一个重定向 *告诉浏览器，再去访问另一个网址*

![1560839639584](Request&Response.assets/1560839639584.png)

- django.http.JsonResponse()——序列化

![1560840145075](Request&Response.assets/1560840145075.png)

