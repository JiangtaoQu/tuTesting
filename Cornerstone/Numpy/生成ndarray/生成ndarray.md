# 生成 ndarray

n 维数组

![1556505902805](生成ndarray.assets/1556505902805.png)

- object——**数组**或嵌套的**数列**

![1556506532920](生成ndarray.assets/1556506532920.png)

![1556506371746](生成ndarray.assets/1556506371746.png)

- dtype——数组元素的数据类型，可选

![1556506648467](生成ndarray.assets/1556506648467.png)

![1556506658670](生成ndarray.assets/1556506658670.png)

![1556509254734](生成ndarray.assets/1556509254734.png)

- copy——对象是否需要复制，可选

- order——创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）

- subok——默认返回一个与基类类型一致的数组

- ndmin——指定生成数组的最小维度

![1556506611798](生成ndarray.assets/1556506611798.png)

![1556506620669](生成ndarray.assets/1556506620669.png)

`ndarray.shape`——数组的维度，对于矩阵，n 行 m 列

![1556509118471](生成ndarray.assets/1556509118471.png)

![1556509127474](生成ndarray.assets/1556509127474.png)

`ndarray.size`——数组元素的总个数，相当于 .shape 中 n*m 的值

![1556509375864](生成ndarray.assets/1556509375864.png)

![1556509386337](生成ndarray.assets/1556509386337.png)

## 生成函数

`ny.zeros(【ndarray.shape】)`——全 0 数组

![1556509903514](生成ndarray.assets/1556509903514.png)

![1556509939605](生成ndarray.assets/1556509939605.png)

`ny.ones(【ndarray.shape】)`——全 1 数组

![1556510422654](生成ndarray.assets/1556510422654.png)

![1556510433627](生成ndarray.assets/1556510433627.png)

`ny.full(【ndarray.shape】【fill_value】)`——全 n 数组

![1556510690261](生成ndarray.assets/1556510690261.png)

![1556510737036](生成ndarray.assets/1556510737036.png)

![1556510741287](生成ndarray.assets/1556510741287.png)

`ny.eye(【ndarray.shape】)`——对角线都是 1，其他都是 0

- n——返回矩阵的行数
- M——返回矩阵的列数，默认为 n
- k——对角线的索引
- dtype——数据类型

![1556511459592](生成ndarray.assets/1556511459592.png)

![1556511673486](生成ndarray.assets/1556511673486.png)

![1556511695095](生成ndarray.assets/1556511695095.png)



`np.astype(【数字类型】)`——转换数组的数据类型

![1556518884382](生成ndarray.assets/1556518884382.png)

![1556518908743](生成ndarray.assets/1556518908743.png)

