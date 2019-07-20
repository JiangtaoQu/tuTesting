# ORM 常用字段

AutoField——int 自增

IntegerField——整数类型 *存不了手机号*

CharField——字符类型 *必填 max_length*

Foreignkey——外键

- to——关联的表
- on_delete——做级联操作删除

DateField——datetime.date()——日期

DateTimeField——datetime.datatime()——

- auto_now_add——创建的时间
- auto_now——每次修改的时间

DurationField——datetime.timedelta()——时间间隔

DecimalField——10进制小数

- max_digits——总长
- decimal_places——小数位长度

## 字段参数

null——可以为空

unique——唯一

db_index——建立索引

default——默认值

to——关联的表

related_name——反查

on_delete=

- model.CASCADE——自动操作
- model.SET_NULL——与之关联设置为 null *所以必须有 null*
- model.SET_DEFAULT——与之关联设置为 默认值 *所以必须有 default*

