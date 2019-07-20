# Hash

> 存储对象

## 报错

![1558680484004](Hash.assets/1558680484004.png)

`config set stop-writes-on-bgsave-error no`

## 增

- `hset 【K】 【F】 【V】`——设置属性和值

![1558680803684](Hash.assets/1558680803684.png)

- `hmset key 【F1】 【V1】 【F2】 【V2】 `——设置多个属性多个值

![1558680821730](Hash.assets/1558680821730.png)

## 查

- `hkeys 【K】`——获取指定键的所有属性

![1558681060196](Hash.assets/1558681060196.png)

- `hget 【K】 【F】`——获取一个属性的值

![1558681288367](Hash.assets/1558681288367.png)

- `hmget 【K1】 【F1】 【K2】 【F2】`——获取多个属性的值

![1558681319240](Hash.assets/1558681319240.png)

- `hvals 【K】`——获取所有属性的值

![1558681501543](Hash.assets/1558681501543.png)

## 删

- `hdel 【K】 【F】`——删除某个属性

![1558681763300](Hash.assets/1558681763300.png)

