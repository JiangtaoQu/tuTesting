# Inspector

## 所需功能

- `platformName`:`Andriod`

- `platformVersion`:`5.1.1`

![1563191401876](Inspector.assets/1563191401876.png)

- `deviceName`:`127.0.0.1:62025`

![1563192850017](Inspector.assets/1563192850017.png)

- `appPackage`:`com.foundao.xinhua_android`

`"C:\Users\Quantum\Documents\Environment\Android\SDK\build-tools\29.0.1\aapt.exe"`

```bash
cd "C:\Users\Quantum\Documents\Environment\Android\SDK\build-tools\29.0.1\aapt.exe"

aapt.exe dump badging 【apk 储存路径】 | find "package"
```

![1563193315487](Inspector.assets/1563193315487.png)

- `appActivity`:`com.foundao.xinhua_android.ui.SplashActivity`

```bash
aapt.exe dump badging 【apk 储存路径】 | find "launchable-activity"

```

![1563193481457](Inspector.assets/1563193481457.png)

- 另一种获取

```bash
adb shell

logcat | grep cmp=

# 打开夜神模拟器，点开 app
```

![1563193987675](Inspector.assets/1563193987675.png)

- `noReset`:`true`——第二次启动再添加 **布尔值**

![1563195073319](Inspector.assets/1563195073319.png)

## 开启会话

![1563195031841](Inspector.assets/1563195031841.png)

com.tal.kaoyan/com.kaoyan.kylogin.ui.info.PerfectInformationActivity

