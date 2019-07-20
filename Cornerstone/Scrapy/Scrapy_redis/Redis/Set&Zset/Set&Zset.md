# Set

## 增

- `sadd  【K】 【member1】 【member2】`——添加元素

![1558685182923](Set&Zset.assets/1558685182923.png)

## 查

- `smembers 【K】`——返回所有元素（无序）

![1558685166393](Set&Zset.assets/1558685166393.png)

## 删

- `srem 【K】 【member1】 【member2】 `

![1558685220759](Set&Zset.assets/1558685220759.png)

# Zset

## 增

- `zadd  【K】 【score1】 【member1】 【score2】 【member2】`——添加元素（依照权重排序）

![1558685664276](Set&Zset.assets/1558685664276.png)

## 查

- `zrange 【K】 【start】 【stop】`——返回所有元素（无序）

![1558685678532](Set&Zset.assets/1558685678532.png)

- `zrangebyscore 【K】 【min】 【max】`——查找权重区间的元素

![1558686071247](Set&Zset.assets/1558686071247.png)

- `zscore 【K】 【member】`——获取权重的值

![1558686876749](Set&Zset.assets/1558686876749.png)

## 删

- `zrem 【K】 【member1】 【member2】`——删除指定元素

![1558686966367](Set&Zset.assets/1558686966367.png)

- `zremrangebyscore 【K】 【min】 【max】`——删除权重在指定范围的元素

![1558687108909](Set&Zset.assets/1558687108909.png)

