#连接示例
# import pymysql  #导入pymsql
# def query(sql):
#     # 连接数据库,(内容为connet方法绑定)
#     db = pymysql.connect(host='127.0.0.1',user='root',password="123456",db='class_base')
#     # 获取查询窗口:游标
#     cur = db.cursor()
#     # 执行sql语句
#     cur.execute(sql)
#     # 获取所有结果
#     res = cur.fetchall()
#     # 关闭连接
#     db.close()
#     return res
# a= query('SELECT * FROM t_chengji WHERE s_name ="张1"')
# print(a)

import pymysql
def linkdb(sql):
    db = pymysql.connect(host='127.0.0.1',user='root',password="123456",db='class_base')
    cur=db.cursor()
    cur.execute(sql)
    res=cur.fetchall()
    db.close()
    return res

if __name__ =="__main__":
 sp=input('请输入商品名:')
 a = linkdb("SELECT sp_mon FROM sp_phone WHERE sp_list='{}'".format(sp))
 print(a)
 if int(a[0][0])>=5488:
    print('买不起')
 else:
    print('买!')

Name='123'
def add():
 s_1= int(input())
 s_2= int(input())
 sum=s_1+s_2
 return sum#方法不写返回值引用打印的时候回默认返回None