# 安装
>1.将mysql文件夹下的bin文件夹地址配置到环境变量的path中
2.管理员打开cmd
3.mysqld -install 安装(sc delete mysql 删除数据库)
4.mysqld --initialize-insecure 初始化数据库,无提示则成功
5.net start mysql 启动数据库.(net stop mysql 停止数据库)

### 用户管理
	默认用户root

>-主机,限制登陆点,
-localhost为仅本机可登陆,%为所有ip都可登陆,其余ip为仅对应ip可登陆数据库

### 创建数据库
#### 图形界面
 >-数据库名(全英),必须字母开头,不能有下划线之外的符号,不能用保留字段如(mysql)
 -字符集,字库(选择中文字库才能在数据库储存中文)
	utf8
	utf8mb4 (优先选择)
#### 终端命令符
>create database 库名 default charset utf8mb4 
创建数据库,同时设定字符集为utf8mb4
drop database 库名 
删除数据库
alter database 库名 default charset utf8mb4
修改数据库,数据库名创建就不能更改 只能修改字符集 
### 制作表
#### 图形界面
>-字段名(单列数据名)-字段名(全英),必须字母开头,不能有下划线之外的符号,不能用保留字段如(mysql)
-字段类型(单列可输入的字符类型)-int(整数)会拿来做加减乘除运算的字段内容为int,varchar(字符串)电话号是字符串
-字段长度(单行单个数据最大内存)-汉字一个2-4bit,英文数字为1bit
-是否为空(null/not null)
-注释-工作台下端,单列数据的备注
-索引-index
-方法(默认)-让字段的值变成自动的(自动获取),时间戳用now()方法即为获取填入时间戳
-主键(唯一识别)-primary key
-操作数据 增 删 改 查 通过下端快捷按键实现
#### 终端界面
> create table 表名(字段1信息,字段2信息);
例:create tablexx (id int(16) not null auto_increment primary key default 1 comment "学号" ) 创建表xx(id字段类型为int(16b字段大小) 不能为空 自动递增 主键 默认值1 注释为学号)
默认值可不设置,方法直接添加不需要声明 自动获取或者获取时间戳(now());


# 通过终端操作(cmd类字符界面)
### 连接数据库
>mysql -h ip地址 -P 端口 -u 用户名 -p 等待弹出输入密码
mysql -h localhost -P 3306 -u root -p 然后等号输入密码  
退出直接exit 本机msql数据库登陆
本机可不输入ip和端口,直接输入用户密码即可

>-IP地址(host)
默认localhost(-h) 
-端口(Prot)
	默认3306(-P)
-账号(user)
 用户名(-u)
-密码(password)
	密码(-p)
### 终端管理数据库(终端操作sql语句后必须跟英文分号";")
>-查看数据库列表
	show databases;

>-选择数据库
	use 数据库名;

  >  -查看表
show tables;查看表列表
desc 表名 
查看表结构(包括字段类型的基本设置)
### 终端界面操作
#### 对表进行操作(会改变表结构)
>-创建
create table 表名(字段信息1,字段信息2);
 -添加索引(index)
 alter table 表名 add index(字段名);
 -删除索引
 alter table 表名 drop index 字段;
 -删除字段
 alter  table 表名 drop 字段;
 -修改表名
 alter  table 表名 rename 新表名;
 -删除表
 drop table 表名;
 >>修改表 
 alter table 表名+修改内容
 -新增字段 
 alter table 表名 add 字段信息
 例:alter table t_xx age int(16) not null default 18;在表t_xx中新增age字段,类型为int长度16,不能空,默认18
 -修改字段名
 alter table 表名 chenge 要改的字段名 新的字段信息
 新字段信息不需要括号,直接将信息陈列在后即可
 -修改字段属性
 alter table 表名 modify 字段名 新的的字段信息;
 此方法不能修改字段名,新的字段信息直接陈列,不需要括号
 -修改字段位置
 alter table 表名 modify 字段名 新字段信息 after 字段名2
将字段修改字段信息的时候将其移动到字段名2的后面





#### 对表内容进行操作(不改变表结构)
##### 查
>-查整表  
select * from 表名;

>-查字段 
select 字段名 from 表名;
多字段直接在字段名后加,字段名,字段名

>-按条件查 
select * from 表名 where 条件(字段内容,字符串需要引号如sex="女" )(多条件搜索直接在分号前加 and 条件(如and age>13);
##### 多表联查(多表之间两两相关即可互相关联查)
>内关联 (取有数值的交集部分)
>>-字段1为两表之间相同字段,显示所有相关字段
select * from 表名1 join 表2 on 表1.字段1 = 表2.字段1; 
三表以上最好相关条件不是一个
>>-按条件进行多表联查
select * from 表名1 join 表2 on 表1.字段1 = 表2.字段1  where 表1.字段1条件 and 表.字段2条件;
>>-显示特定表的特定字段的同时整理相关性条目,字段1和2为两表之间相同字段,3表以上联动 两两相关即可
select 表名.字段,表名.字段,表名.字段, from 表名1 join 表2 on 表1.字段1 = 表2.字段1 join 表3 on 表3.字段2= 表1(或表2).字段2;

>外关联
以join为界,左为左关联(left join),右为右关联(right join),区别在于查询时以对应表的内容为主显


##### 增,删,改	
>-增加整条条目;
insert into 表名 (字段1,字段2) values (值1,值2);

>-删除条目
delete from 表名 where 字段 = 值;

>-修改条目
update 表名 set 字段1=值 ,字段2=值 where 字段 =值;(不加条件即整个字段全部修改)

### sql常见技巧
#### as  结构为 表(或字段名) as 昵称
	给某个数据取别称,在语句中可以省略as,直接在语句中后接昵称就行,取别称可在任意处取,但是要取名表单独出现的地方,做表名.字段名时不可用,且要整表更改
#### order by 排序
	desc 倒序(从大到小)
	在结构倒数第二行 order by 排序字段 desc,即可按排序数据倒序,多表查询中 字段前也需要加表名
	asc(省略不写,默认就是倒序)
	
#### limit 限制显示数量
	直接在句子最后加上 limit 0,x (意思为显示从第0条显示,一共显示x条)
#### 运算
	直接在查找目标段用运算式表示目标
	例,select a,b,c,a+b-c from 表名.....order by a+b-c  limit 0.x(从表名中查询abc并运算然后按运算结果从小到大正序排列并从结果第0行开始x行)  a+b-c的语句可以给与昵称


#### group by 分组(必须配合聚合函数) 只能显示用来分组依据的字段和函数字段
	格式:select 字段,函数(字段) from 表 group by 字段;
	     having 类似where的条件筛选,但是只能用在group by后面
	例:select sname,count(*) from 表 group by sname having count(*)>1:查找表中sname的数据并计数,显示分组显示计数结果大于1的sname结果

#### 聚合函数(都是以列为单位操作)
	sum
		求和
			select sum(字段) from 表; 可在from前插入多个计算函数
	max
		求最大值
	min
		球最小值
	avg
		求平均值
	count
		计数
			select count(字段) from 表  ,计算表中字段中有多少条数据,空值null会省略


##### 判断条件 (多条件后面直接and 加条件再分号结尾)
> 不等于 !=
等于 =
大于和大于等于 >,>=
小于和小于等于 <,<=

>在 in 
select * from 表名 where 字段名 in (1,3,5,7);
查找表中id在(1,3,5,7)其中的内容,查询不在的直接将in替换为 in not

>是 is
 select * from t_表名 where 字段名 is null;
 判断类型,通常只用来判断是否为空,空值=无数据,只能用is(is取反为 is not)

>介于xx和xx中间 between (用于可以比较大小的数字之间)
select * from t_表名 where 字段名 between 字段值 and 字段值;
(同时做对比的两个字段值也会显示在结果中, 取反为not between)

>包涵 like  (多用在字符串)
select * from t_表名 where 字段名 like "xxx%";
查询字段中xxx开头的条目,
"%xxx"则为以xxx结尾的语句,
"%xxx%"为只要包涵xxx就列出,
%%%为无条件,既显示所有

> and和or
多用于多条件查询中表达多条件的存在关系,并列和二选一即可

> 运算符+ - x /
%(取余) 例:"where xx % 2=1;"当xx除去2余1的时候

### 条件语句
>case when条件 then 执行 end
select id,sname,case when classid=1 then "一班"  when classid=2 then "二班"  else "未知" end  from t_student
当班级表中班级id等于1和2是将其显示一班,二班,其余变为未知,一个case只能在表单中生成一个字段,要实现同一字段内的对比,可用多case条件实现分列,然后通过虚拟表进行对比

#### 通过条件语句来实现子查询
>select * from t_student where id in(select id from t_student  where sex="女") 
查询满足在括号条件的id的全部信息 作为条件时()内只能用一个字段

>select * from (select id sname ,(select id,sname,case when classid=1 then "一班"  when classid=2 then "二班"    else "未知" end ) as class   from t_student) a where class="一班" 
 将 case查询生成的虚拟表当做实体表class进行查询

### 事务(悔棋功能)
> begin(开始)
commit(确认)   rollback(回滚)
确认和回滚都是结束事务,确认直接保存,回滚返回到开始命令之前, 三命令都是直接输入即可,

## 表的分类

### 真实表
 真实存在于数据库的表 
###临时表
>临时创建的表单,和真实表一样使用,但在数据库中查询(show tables)不到,且断开数据库再连之后会消失
创建语句
create temporary table 表名(字段信息);
### 虚拟表
>通过查询生成的结果表单,将其通过子查询进行套娃查询即可实现虚拟表的使用
例:
1,select * from t_student where id in(select id from t_student  where sex="女") 
查询满足在括号中虚拟表的id的全部信息 
作为条件时()内只能用一个字段,
2,select * from (select id sname ,(select id,sname,case when classid=1 then "一班"  when classid=2 then "二班"    else "未知" end ) as class   from t_student) a where class="一班"  
将 case查询生成的虚拟表当做实体表class进行查询



