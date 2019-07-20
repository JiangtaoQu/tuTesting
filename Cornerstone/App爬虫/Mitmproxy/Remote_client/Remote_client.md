# Remote_client

1. 不要开启桥连

![1558440328448](Remote_client.assets/1558440328448.png)

2. 查看虚拟机 IP

![1558345910753](Remote_client.assets/1558345910753.png)

3. 修改模拟器 IP

![1558346125017](Remote_client.assets/1558346125017.png)

4. 安装证书

![1558353634603](Remote_client.assets/1558353634603.png)

5. 清空 mitmproxy

![1558353776191](Remote_client.assets/1558353776191.png)

6. 过滤—— f

![1558354046058](Remote_client.assets/1558354046058.png)

`!(~c 200)`——非 请求为200

`~d baidu.com`——请求跟 baidu 有关的

`~m post & ~u baidu.com`——所有 post 和 url 包含 baidu 的

7. 断点拦截—— i

`~d baidu.com & ~m get`——拦截 baidu 和 get 的请求

![1558354978795](Remote_client.assets/1558354978795.png)

8. 修改 request —— e

![1558440712217](Remote_client.assets/1558440712217.png)

![1558440839052](Remote_client.assets/1558440839052.png)

![1558440988449](Remote_client.assets/1558440988449.png)

![1558441043033](Remote_client.assets/1558441043033.png)

9. 修改 response —— e

![1558441444964](Remote_client.assets/1558441444964.png)

![1558441498851](Remote_client.assets/1558441498851.png)

## mitmdump

1. mitmdump

![1558441807312](Remote_client.assets/1558441807312.png)

2. `mitmdump -s new.py`

![1558442170442](Remote_client.assets/1558442170442.png)

3. 打开 py 文件

![1558442067514](Remote_client.assets/1558442067514.png)

![1558442344585](Remote_client.assets/1558442344585.png)

4. 启动安卓模拟器，接收数据

![1558442594337](Remote_client.assets/1558442594337.png)

5. 打印日志

 ![1558442693520](Remote_client.assets/1558442693520.png)

```python
from mitmproxy import ctx

def request(flow):
	# print(flow.request.headers)
	ctx.log.info(str(flow.request.headers))
	ctx.log.warn(str(flow.request.headers))
	ctx.log.error(str(flow.request.headers))
```

![1558442822185](Remote_client.assets/1558442822185.png)

![1558443395671](Remote_client.assets/1558443395671.png)

```python
from mitmproxy import ctx


def request(flow):
    # print(flow.request.headers)
    ctx.log.info(str(flow.request.headers))
    ctx.log.warn(str(flow.request.url))
    ctx.log.warn(str(flow.request.host))
    ctx.log.error(str(flow.request.method))
    ctx.log.error(str(flow.request.path))


def response(flow):
    ctx.log.error(str(flow.response.status_code))
    ctx.log.error(str(flow.response.text))
```

