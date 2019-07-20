# String

1. 以二进制储存

2. maxlength——512M

3. redis-cli.exe——启动

![1558602911209](String.assets/1558602911209.png)

4. `ping`——检查

![1558602972072](String.assets/1558602972072.png)

5. `select 【index】`——选库（默认为0）

![1558603131432](String.assets/1558603131432.png)

## 增

- `set 【K】 【V】`——字段

![1558603121268](String.assets/1558603121268.png)

- `get 【K】`——获取对应键的值

![1558603158951](String.assets/1558603158951.png)

### 时效

- `setex 【K】 【S】 【V】`——设置键值及过期时间（秒）

![1558603218208](String.assets/1558603218208.png)

- `mset 【K1】 【V1】 【K2】 【V2】`——设置多个键值

![1558603421719](String.assets/1558603421719.png)

## 查

- `mget 【K1】 【K2】`——获取多个值

![1558603654451](String.assets/1558603654451.png)

- `append 【K】 【V】`——追加值

![1558603545517](String.assets/1558603545517.png)

## 键命令

- `keys 【pattern】`——查看所有的键

![1558603885381](String.assets/1558603885381.png)

![1558603919383](String.assets/1558603919383.png)

- `exist 【K】`——判断是否存在

![1558604106222](String.assets/1558604106222.png)

- `type 【K】`——查看键对应的值的类型

![1558604191524](String.assets/1558604191524.png)

- `del 【K1】 【K2】`——删除键及对应的值

![1558609307651](String.assets/1558609307651.png)

- `ttl 【K】`——查看有效时间

![1558609200419](String.assets/1558609200419.png)

- `expire 【K】 【S】`——设置键的过期时间 *不要设置已经设定过的*

![1558609765042](String.assets/1558609765042.png)

