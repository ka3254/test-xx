# DQL数据查询语言
>不会导致真实表改变
>>select 
>- select * from 表名;查整表
>- select 字段名,字段名from表名
>- 按条件查 select * from 表名 where 条件(字段内容,字符串需要引号如sex="女");(多条件搜索直接在分号前加 and 条件(如and age>13;)
>>多表联查
>- select * from 表名1 join 表2 on 表1.字段1 = 表2.字段1;  字段1为两表之间相同字段,显示所有相关字段
>- select 表名.字段,表名.字段,表名.字段, from 表名1 join 表2 on 表1.字段1 = 表2.字段1 join 表3 on 表3.字段2= 表1(或表2).字段2;  
字段1和2为两表之间相同字段, 显示特定表名加字段的同时整理相关性条目,3表以上联动 两两相关即可 多表联查最好不要多个相关条件是一个
>- select * from 表名1 join 表2 on 表1.字段1 = 表2.字段1  where 表1.字段1条件 and 表.字段2条件; 按条件进行多表联查

-from

-where

# DML数据操纵语言
>导致数据变动的语句
>>insert 
>- insert into 表名 (字段1,字段2) balues(值1,值2);
>>delete 
>- delete from 表名 where 字段 = 值;
>>-update
>- updata 表名 set 字段1=值,字段2=值 where 字段=值;


# DDL数据定义语言
>和数据库结构相关
>>create创建
>- carete database 库名  default charset utf8mb4
>- create table 表名(字段信息1,字段信息2)
>- create temporary 表名(字段信息,字段信息);
创建临时表;
--字段信息(字段名 字段类型(字段长度)<int,varchar> 是否为空 方法<now()/auto_increment> 主键<primary key,> 默认值<default,> 注释 <comment,>  )
>>alter修改
>- alter database 库名 default charest utf8mb4
>- alter table 表名  修改内容
alter table 表名 add 字段(字段信息)(此处字段信息不需要括号)
alter table 表名 chenge 要修改的字段名 新的字段名
alter table 表名 modify 要修改的字段 新的字段信息(此方法不能修改字段名)
alter table 表名 add index(字段名)
alter table 表名 drop index 字段
alter table 表名 drop 字段名
alter table 表名 rename 新表名
>>drop删除
>- drop database 库名
>- drop table 表名

# DCL数据控制语言
>控制数据库功能的语句
>- begin 
开始事务
>- commit
确认事务
>- rollback
回滚到开始之前


# 其他语句
>登录数据库
 mysql -h xxxx -P xxxxx -u xxx -p

 >数据库使用
 >- show databases;
 >- use databas 库名

>表查看
 >- show tables;
 >- desc 表名; 显示选择表格的设置(字段设置)
 
 >as语句(对表,或者条件给于昵称)
 >- xxx as a, as通常简化不写,并且as可以用在任何该条目单独存在的地方.
 例: t_xx t   将t_xx简称为t,

 >order by 排序
 >- order by 字段名 desc;按照字段的大小进行从大到小的倒序排列,正序时用asc或者不用orderby,sql默认排序为正序,仅用于可比较大小的数字字段.

 >limit 限制显示数量
 >- limit 0,x;c从0条开始显示到第x行,第0行为标题行.

 >group by 分组
 >-  必须配合聚合函数,只显示用来做分组的字段主体和函数字段,同时分组字段会被设置成类似主键的不重复,
 >- 格式 select 字段 函数(字段1) from 表 group by 字段;
 >- having:类似where的条件筛选,但是只能用在group by后面
 例子:例:select sname,count(字段) from 表 group by sname having count(字段)>1;查找表中sname的数据并计数,显示分组显示计数结果大于1的sname结果
 >-  sum函数 求和
 select sum(字段) from 表; 可在from前插入多个计算函数
 >- max 求最大值 
 >- min 求最小值
 >- avg 求平均值
 >- count 计数 
 select count(字段) from 表  ,计算表中字段中有多少条数据,空值null会省略

# 条件语句
>- case when 条件 then 做什么 end
        when 条件 then 做什么 end
   例:select id,sname,case when classid=1 then "一班"  when classid=2 then "二班"  else "未知" end  from t_student;
>>- case语句来分列
SELECT
			s.id,
			MAX(case when c.name="语文" then sc.score END) chinese,
     MAX(case when c.name="数学" then sc.score END) math /*查询出单科成绩
		FROM
			student s
		JOIN sc ON s.id = sc.sid
		JOIN course c ON c.id = sc.cid
GROUP BY s.id  将同列的成绩数分列出来, 

