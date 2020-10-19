import requests
from tools.dbtools import linkdb
# #python调接口
# #1.构造请求
u='http://118.24.105.78:2333/get_title_img'
r= requests.get(u)
# print(r.text)
# #2.判断结果:断言实现判断http状态码和结果码
assert r.status_code ==200 #判断状态码是否等于200
# r.json()将结果转换成字典
assert r.json()['status'] == 200 #判断结果码是否正确,需要在状态码正常的情况下才能进行,结果码是可以被人员修改的
# assert 1>2

# 3.数据库校验:本次要查询所有轮播图id是否存在
data=r.json()['data']
for i in data:
  print(i['id'])
#   每获得一次id就去数据库进行一次id为条件的查询
  sql='select * from t_title_img where id={}'.format(i['id'])
  res= linkdb(sql)
  print(res)
# 断言判断返回值不为空,为空则报错,有bug
  assert len(res) !=0
  print('成功')

