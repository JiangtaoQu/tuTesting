# ADB

`"C:\Users\Quantum\Documents\Environment\Android\SDK\platform-tools\adb.exe"`

- `adb start-server`——启动 adb 服务器

```bash
adb start-server
# 如果没启动
adb nodaemon server
# 查看进程
netstat -ano | findstr "5037"
# 如果被占用 杀死
taskkill -f -pid "5037"

adb start-server
```

![1563107189224](ADB.assets/1563107189224.png)

- `adb kill-server`——结束服务

- 启动开发者模式

![1563107307535](ADB.assets/1563107307535.png)

![1563107386705](ADB.assets/1563107386705.png)

![1563107431522](ADB.assets/1563107431522.png)

- `adb version`——查看版本

![1563107578514](ADB.assets/1563107578514.png)

- `adb devices`——查看连接设备

- 同步 adb 

1. `...Android\SDK\platform-tools`

![1563107708907](ADB.assets/1563107708907.png)

2. `…\Nox\Nox\bin`——夜神 内三个同样文件备份

![1563107891469](ADB.assets/1563107891469.png)

3. 覆盖

![1563108048146](ADB.assets/1563108048146.png)

4. `adb version`——查看版本

![1563108118539](ADB.assets/1563108118539.png)

5. `nox_adb`备份，复制 adb.exe 更名为 nox_adb

![1563108195582](ADB.assets/1563108195582.png)

6. `adb devices`——查看连接设备

![1563108566397](ADB.assets/1563108566397.png)

- `adb -s 【设备名】 shell`——进入设备操作系统

![1563108911111](ADB.assets/1563108911111.png)

- `adb -s 【设备名】 install 【apk 路径】`——安装 apk 包

- `adb -s 【设备名】 uninstall 【包名】 `——卸载

```bash
# 查看包名
adb -s 【设备名】 shell

cd /data/app

ls

exit
```

- `adb shell pm list package`——查看系统包名

![1563109469049](ADB.assets/1563109469049.png)

- `adb push 【真机文件路径】 【设备存储位置】`——真机传递文件到设备

- `adb pull 【设备文件路径】 【真机存储位置】`——设备传递文件到真机

- `adb shell screencap 【存储位置】`——设备截图

