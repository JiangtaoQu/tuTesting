# Datetime

- `datetime.date`——表示日期的类

- `datetime.time`——表示时间的类

![1562979520484](Datetime.assets/1562979520484.png)

- `datetime.now()`——返回当前日期和时间

![1562979690998](Datetime.assets/1562979690998.png)

![1562979701978](Datetime.assets/1562979701978.png)

- `datetime(【date】)`——Struck time→Format string，构建指定日期和时间

![1562979830499](Datetime.assets/1562979830499.png)

![1562982535636](Datetime.assets/1562982535636.png)

- `datatime(strptime(【str】,【'%Y-%m-%d %H:%M:%S'】))`——Str→Format string——用户输入的日期和时间是字符串，要处理日期和时间，首先必须把 str 转换为 datetime

![1562983050609](Datetime.assets/1562983050609.png)

![1562983187670](Datetime.assets/1562983187670.png)

- `datetime.strftime(【datetime】,【'%Y-%m-%d %H:%M:%S'】)`——Format string→Str——要把它格式化为字符串显示给用户，就需要转换为 str

![1562983152926](Datetime.assets/1562983152926.png)

![1562980516691](Datetime.assets/1562980516691.png)

- `【datetime】.timestamp()`——Strucktime→Timestamp，timestamp是一个浮点数。如果有小数位，小数位表示毫秒数

![1562982645012](Datetime.assets/1562982645012.png)

![1562980749600](Datetime.assets/1562980749600.png)

- `datetime.fromtimestamp(【date】)`——Timestamp→Struck time

![1562981050203](Datetime.assets/1562981050203.png)

![1562981066986](Datetime.assets/1562981066986.png)

- `timedelta()`——时间差

![1562982078882](Datetime.assets/1562982078882.png)

![1562982778215](Datetime.assets/1562982778215.png)

![1562982962945](Datetime.assets/1562982962945.png)

- `tzinfo=timezone(timedelta())`——转换时区

![1562982855367](Datetime.assets/1562982855367.png)

![1562982946938](Datetime.assets/1562982946938.png)

