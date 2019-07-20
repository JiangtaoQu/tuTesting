# IP代理池

- middlewares——`request.meta['proxy'] = 'http://' + proxy`

  ![1563537785672](IP代理池.assets/1563537785672.png)

```python
import random


class IPProxyDownloadMiddleware:
    PROXIES = [
        '178.44.170.152:48182',
        '60.167.20.253:20701',
        '111.177.164.37:37485',
    ]

    def process_request(self, request, spider):
        proxy = random.choice(self.PROXIES)
        if request.url.startswith('http://'):
            request.meta['proxy'] = 'http://' + proxy
        elif request.url.startswith('https://'):
            request.meta['proxy'] = 'https://' + proxy
```

- settings

![1557926570131](IP代理池.assets/1557926570131.png)

- spider

![1557926609346](IP代理池.assets/1557926609346.png)

| IP 类型      | 透明 | 匿名 | 高密 |
| ------------ | ---- | ---- | ---- |
| 得知使用代理 | √    | √    | ×    |
| 得知真实 IP  | √    | ×    | ×    |

