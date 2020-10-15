# bug的定位和抓包
## bug的定位
### 功能测试中bug的定位
>1.没有用到接口(没有抓到包)
>- 前端bug
>- 前端代码报错-前端bug
>
>2.用到接口:看状态码
>- 200-前端bug(前提是接口已经测试ok了)
>- 400,404,405-前端bug(使用接口的语句错误)
>- 500-后端bug
### 接口测试(后端)中bug的定位
>1.接口报500
>- 找到对应错误日志(服务器中tail-f)
>
> 2.报200
>- 提示信息是否准确
>- 检查返回数据是否和数据库数据一致
>1.sql语句不正确,
>2.提供正确sql语句给开发
___
## 抓包
>- 1.捕获前端发送给后端的数据的过程叫抓包
   2.抓其他设备的包只需要将其在同一局域网设置wifi的高级设置,代理设置,将抓包软件安装端的ip设置为代理即可实现
### 抓包工具   
#### fiddle(更改系统设置后都需重启)
##### 抓包方法
>- 基础设置
>tools->options->https安装证书
>- 启用筛选
filters->勾选use filters->点选第二行下拉框选择show only the followinghost
在输入框写入抓包地址,多地址分号隔开(例:'*bilibili.com;')
>- 弱网测试
>选择rules->customiz rules,在弹出框中找到下放字段:
			      if (m_SimulateModem) {
            // Delay sends by 300ms per KB uploaded.
            oSession["request-trickle-delay"] = "300"; 
            // Delay receives by 150ms per KB downloaded.
            oSession["response-trickle-delay"] = "150"; 
        }  修改直接修改数字,单位为kb
>- 抓手机的包(手机电脑需在同一局域网)
> 1.tools-options-connection-勾选allow remote,fiddler listens 设置为8888(端口号)
>2.安装证书,在浏览器进入fiddler所在电脑的ip+8888端口,此处端口和fiddler设置相同(ip:8888)下载证书安装
>3.代理设置,进入wifi-修改网络-显示高级选项-服务器主机,电脑ip,端口8888,保存
>4.手机代理之后无法上网就在 rules-customiz rulues的OnBeforeRequest方法里加上如下语句:
>if (oSession.host.toLowerCase() == "webserver:8888") 
>{  oSession.host = "webserver:80";}
#### 浏览器自带工具(F12)
>-抓包工具/network
>-调整功能/console
>-缓存/application--cookies
>-审查元素/elments
## adb(专用于安卓的测试工具)
### 连接方法
>- adb安装完成之后需要配置adb文件夹的bin文件夹到环境变量
>- adb version检查 adb版本号确认是否安装成功
>- 在连接手机的开发者选项中打开usb调试之后 在终端输入adb devices 显示连接设备
### 操作方法
> 进入adb shell之后的命令不需要加 adb sehll前缀
>- 安装软件到手机
adb install 安装包.apk(输入完前置命令后直接将安装包拖入cmd页面)
>- 查看已安装的软件
adb shell pm list packages (显示所有软件)
adb shell pm list packages -3 只显示第三方安装软件
>- 卸载
adb uninstall 查出来的软件名
>- 移动文件
手机->电脑:adb pull 目标(带路径) 位置
电脑->手机:adb push 目标(带路径) 位置
### ★adb shell(命令行输入)类命令
>- adb shell:终端进入手机系统
进入sdcard/ 进入手机内存,adb shell命令与linux命令基本一致
>- ps-ef(adb shell ps-ef)
查看任务列表/运行状态
>- top(adb shell top)系统资源监控
显示软件占用内存资源的情况
res/内存
shr/运存
s状态 s-休眠 r-运行
>- top -d l|grep 软件名 
动态显示该软件的资源使用情况,ctrl+c停止
>- dumpsys battery
电池监控
>- monkey -p 软件名 -vvv 次数
自动运行软件
>- adb shell monkey -p 软件名 -vvv-次数 >f:\日志.txt
自动运行软件的同时储存日志到f的日志文档里
### 日志处理
>- adb logcat >日志名(带路径)
将运行日志保存为日志文件
例:adb logcat >f:\日志.txt
>- 分析日志(在日志文档搜索关键词)
ANR-APP出现卡顿
CRASH-app崩溃
Exception-其他问题




