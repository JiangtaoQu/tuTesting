# Random

## 随机整数

- `random.randint()`——随机 5 >= x >= 1

![1558139802235](Random.assets/1558139802235.png)

![1558139818635](random.assets/1558139818635.png)

- `random.randrange()`——随机 9，7，5，3，1——如果不设置**步长**，和`randint`一样

![1558139870335](Random.assets/1558139870335.png)

![1558139883851](random.assets/1558139883851.png)

## 从一个数据集合里（可以不同类型）随机抽取一个对象

- `random.choice([])`——随机选择**一个**

![1558140135583](Random.assets/1558140135583.png)

![1558140152885](random.assets/1558140152885.png)

- `random.sample([])`——随即返回**多个**

![1558140199397](Random.assets/1558140199397.png)

![1558140208870](random.assets/1558140208870.png)

## 打乱顺序

- `random.shuffle([])`——随机打乱顺序，**直接改变元数据**

![1558140518830](Random.assets/1558140518830.png)

![1558140531894](random.assets/1558140531894.png)

## 例子

### 验证码

```python
import random


def yzhm():
    r = ''
    for i in range(6):
        r1 = random.randint(65, 90)  # 数字转字母
        r2 = random.randint(0, 9)
        ret = random.choice([chr(r1), str(r2)])
        r += ret
    return r


print(yzhm())

```

### 随机user-agent

