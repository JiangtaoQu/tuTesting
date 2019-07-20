```python
import os
import sys

if __name__ == '__main__':
    # 加载 Django 项目的配置信息
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'untitled.settings')
    # 导入 Django 并启动 Django 项目
    import django
    django.setup()
```

==如果不会可以去 manage.py 查看==

