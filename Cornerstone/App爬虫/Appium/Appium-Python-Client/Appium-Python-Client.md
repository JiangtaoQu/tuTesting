# Appium-Python-Client

```bash
pip3 install Appium-Python-Client
```

## 连接

- `webdriver.Remote(command_executor, desired_capabilities)`——连接远端

![1563277964126](Appium-Python-Client.assets/1563277964126.png)

![1563277998824](Appium-Python-Client.assets/1563277998824.png)

- `WebDriverWait(driver, timeout)`——等待判断

![1563278116163](Appium-Python-Client.assets/1563278116163.png)

![1563278100813](Appium-Python-Client.assets/1563278100813.png)

## 滑动方法

- `driver.get_window_size()['width']`——取得屏幕的的宽
- `driver.get_window_size()['height']`——取得屏幕的的高

![1563277585755](Appium-Python-Client.assets/1563277585755.png)

- `driver.swipe(int start x,int start y,int end x,int y,duration) `——滑动

![1563276693729](Appium-Python-Client.assets/1563276693729.png)

- `driver.swipe(x/2, y*3/4, x/2, y/4, 200)`——上滑

- `driver.swipe(x/2, y/4, x/2, y*3/4, 200)`——下滑

- `driver.swipe(x*3/4, y/2, x/4, y/2, 200)`——右滑

- `driver.swipe(x/4, y/2, x*3/4, y/2, 200)`——左滑

