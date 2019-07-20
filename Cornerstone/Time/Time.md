# Time

<ul>
    <li><a href='datetime'>datetime</a></li>
</ul>

### time.sleep()

休眠

### time.time()

时间戳，返回的是**float**类型

### time.ctime(Timestamp)

![1555850801065](Time.assets/1555850801065.png)

![1555850810129](Time.assets/1555850810129.png)

## 表示时间的三种方式

| 表示           | 形式           | 用途         |
| -------------- | -------------- | ------------ |
| 字符串         | **格式化**时间 | 给人看       |
| 时间戳         | float          | 给计算机看   |
| **结构化**时间 | 元组           | 计算时间用的 |

### struct_time

| 索引(Index) | 属性(Attribute)  | 值(value) |
| ----------- | ---------------- | --------- |
| 0           | tm_year          |           |
| 1           | tm_mon           |           |
| 2           | tm_mday          |           |
| 3           | tm_hour          |           |
| 4           | tm_min           |           |
| 5           | tm_sec           |           |
| 6           | tm_wday(weekday) |           |

![1555850942927](Time.assets/1555850942927.png)

![1555850952487](Time.assets/1555850952487.png)

## 格式之间的转换

- Struck time $\rightleftharpoons$ 结构化时间

- Timestamp $\rightleftharpoons$ 时间戳

- Format string $\rightleftharpoons$ 格式化时间

![Snipaste_2019-02-12_18-18-35](Time.assets/Snipaste_2019-02-12_18-18-35.png)

### 时间戳 $\rightarrow$ 结构化时间 localtime() / gmtime()

![1555851137592](Time.assets/1555851137592.png)

![1555851145817](Time.assets/1555851145817.png)

### 结构化时间 $\rightarrow$ 时间戳 mktime()

![1555851312321](Time.assets/1555851312321.png)

![1555851325828](time.assets/1555851325828.png)

### 结构化时间 $\rightarrow$ 格式化时间 strftime()

![1555851494679](Time.assets/1555851494679.png)

![1555851505641](time.assets/1555851505641.png)

### 格式化时间 $\rightarrow$ 结构化时间 strptime()

![1555851633965](Time.assets/1555851633965.png)

![1555851644342](Time.assets/1555851644342.png)

## 时间差

