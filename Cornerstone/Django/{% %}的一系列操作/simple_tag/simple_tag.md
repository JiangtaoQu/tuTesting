# simple_tag

```
from django import templateregister = template.Library()@register.simple_tag()def st(*args, **kwargs):    print(args, kwargs)    return 
```

