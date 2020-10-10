#### 文件属性
> 首字母 - 文件 d 文件夹
  次字幕 r  可读
  三字母 w 可写
  四字母 x 可执行

#### linux的路径
>- cd 进入
>- '/'根目录 
>- '.'当前路径
>- '..'上级路径
>- '~'用户路径
>- 绝对路径:从第一层文件夹开始的完整路径 例: /root/xxx/xxx/文件夹/
>- 相对路径:从当前文件夹直接简写路径  例:   ./文件夹  点代表当前路径
>- pwd 查看当前所在路径

#### 文件读写
> ##### 读取
>- 'cat 文件名' 针对可一次性显示完整的小文件
>- 'more 文件名' 针对需要多屏的大文件,在读取过程中enter键可继续翻页,停止读取按crtl+c撤销命令即可
>- :)'tail -f 日志路径'读取动态日志文件,面试必考,使用时文件会动态变化,ctrl+c退出
>##### 写入
>- 'vi 文件名',通过linux的vi记事本功能实现,
 >- 进入vi文件的界面之后 输入'i'进入编辑模式,同时下方栏框出现 insert 就进入了编辑模式,
 输入完成之后按esc即可退出编辑模式,
 >-  在退出编辑模式之后可以选择保存并退出退出(':wq')或不保存退出('q!'),或者在未对文件进行修改的情况下直接退出('q');

 #### 常用命令
 > ##### 查看文件列表
>- ll 显示当前文件夹下的带详细信息的所有文件列表
>- ls 显示当前文件夹下的所有文件名
> ##### 创建
>- 'touch 文件名' 创建文件
>-  'mkdir 文件夹名' 创建文件夹
> ##### 复制(cp)
>- 复制+改名 'cp 文件 新文件名
>- 复制+移动 'cp 文件 目标路径 (路径绝对相对都可,若文件和目标文件夹在一个目录也可直接写'./文件夹名') 
>##### 移动(mv)
>- 移动文件 'mv 文件 目标路径'
改名 'mv  文件名 新文件名'
>- 移动文件夹 'mv -r 文件夹名 新路径'
重命名文件夹 'mv -r 文件夹名 新文件夹名'
>##### 删除(rm)
>- 文件
rm  文件 会给出确认选项
rm -f 文件 不会给出确认直接删除
>- 文件夹 
rm -r 文件夹 会给出确认选项
rm -rf 文件夹 不会给出选项 直接删除

#### 软件安装
>##### 在线安装
>yun (linux的在线安装工具)
>-yum list(显示yum中的软件)
>- yum install 软件名 安装软件
unzip 解压软件
redis 数据库软件
>- yum remove 软件名 卸载软件
##### 离线安装
>- 安装包(rpm格式)
安装 rpm -ivh 安装包名 
卸载 rpm -e 软件名 
>- 压缩包
1 解压:
 .zip unzip 压缩包名
.tar包 tar xf 压缩包 
.tar.gz tar zxvf 压缩包
>- 使用软件 
直接在软件目录下输入启动器名称启动
linux软件一般放在根目录下usr文件夹
./startup.sh或者 路径/startup.sh
#### linux 系统命令
>##### 查找
>- find 查找范围 -name 文件名
例: find / -name tomcat 在根目录范围下查找tomcat
>- grep 查找内容中的文件通常和其他命令组合使用
> 例:cat 文本|grep 查询内容
cat 日记|grep xx
>- ps -ef 查找任务列表
例: ps -eg|grep tomcat  显示任务列表 并显示和tomcat相关内容
>- kill-9 pid 杀进程
例:kill-9 5514 (杀掉pid为5514的进程,pid可由查找任务列表+grep命令查询获得)
>- rpm -qa 查看软件列表
### redis
>#### 安装卸载
>- 安装 yum install redis
>- 卸载 yum remove redis
>- 检查状态  ststemctl status redis 
>####  连接
>- 启动,断开systemctl start/stop redis
>- redis-cli 
>- redis-cli --raw(带中文参数启动)
>- 进入后修改密码 config set requirepass 123456
>- exit 退出
>- redis desktop manger windos平台redis可视化软件
>- 远程连接
   完成安装之后 linux下查找redis.conf文件,找到bind行下ip,改为0.0.0.0,保存即可 (find / -name redis.conf)设置完成之后需要重启redis
>#### redis的安全相关
>- 设置密码:config set requirepass 密码
>- 输入密码:auth 密码
>-  查看密码:config get requirepass
#### 基本操作
>- 增/改
> set key value 例;set name 张三
>- 改key名
> rename key 新key名
>- 删
del key 例,del name
>- 查 get key 例,get name