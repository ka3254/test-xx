import requests
from tools.dbtools import linkdb
from tools.excel_tools import read_excel
res=read_excel('data.xlsx','登陆')
print(res[0][2])
url=res[0][2]
# 将请求参数写入data
data=eval(res[0][4])#读取到的为字符串,eval()方法强转为字典进行使用
# 将请求头装入h
h=eval(res[0][5])
# 将post请求的返回值装入res
res=requests.post(url=url,json=data)
# 判断状态码是否为200
assert res.status_code==200
# 判断结果码是否正确
assert res.json()['status'] ==200
# 字符串形式显示结果
print(res.text)
# 连接数据库查询账户是否存在并断言判断,存在则打印
# sql='select*from t_user where username="liuyun1"'
# assert len(linkdb(sql)) !=0
# print('接口测试成功')
# 提取出token
token=res.json()['data']['token']
print(token)

# url_1="http://118.24.105.78:2333/inspirer/new"
# header1={"Content-Type":"application/json","token":token}
# data_1={ "content":"156486645647",  "ximg":"dsfsdf.jpg" }
# res1=requests.post(url_1,json=data_1,headers=header1)
# print(res1.text)

