# Mysql连接

- \_\_init\_\_.py——py3要添加

```python
import pymysql

pymysql.install_as_MySQLdb()
```

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'crm',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}
```

