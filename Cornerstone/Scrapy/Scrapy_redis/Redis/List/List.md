# List

## 增

- `lpush 【K】 【V1】 【V2】 【V3】`——左侧插入数据

![1558683310453](List.assets/1558683310453.png)

- `rpush 【K】 【V1】 【V2】 【V3】`——右侧插入数据

![1558683343763](List.assets/1558683343763.png)

- `linsert 【K】 【before|after】 【plvot】 【V】 `——指定元素之前或之后插入新数据

![1558683431824](List.assets/1558683431824.png)

- `lset 【K】 index 【V】`——设置指定索引元素

![1558683697730](List.assets/1558683697730.png)

## 查

- `lrange 【K】 【start】 【stop】 `——查看列表

![1558683465532](List.assets/1558683465532.png)

## 删

- `lrem 【K】 【count】 【V】`
	
	- `lrem 【K】 【0】 【V】`——全部移除
	
	![1558684602878](List.assets/1558684602878.png)
	
	- `lrem 【K】 【+】 【V】`——从头往尾
	
	![1558684552586](List.assets/1558684552586.png)
	
	- `lrem 【K】 【-】 【V】`——从尾往头
	
	![1558684528090](List.assets/1558684528090.png)

