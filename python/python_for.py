'''
# 对数组分类分别填入不同数组
cj =[80,60,59,29,99]
heg=[]
buhe=[]
for i in cj:#for的in遍历取值cj数组,if的in是判断是否存在
    if i<60:
     buhe.append(i)
    else:
     heg.append(i)
print('合格的成绩为{}'.format(heg) + '不合格的成绩为{}'.format(buhe))
'''
'''
# 遍历字典
account = {'name':'张三','成绩':88}
for i in account:
 print(i) #取出key
 print(account.get(i))#获得key对应的值
# for i in account.values(): #只获取values
#   print(i)

# 遍历字符串
aa = "xdadwad"
for i in aa:
    print(i)
'''

# 序列生成器 range(10)->[0,1,2,3,4,5,6,7,8,9]
# for i in range(10):
#     print(i)

# # 用range做下标生成器
# a=[11,22,33,44,66,55,77,88,99,'xx']
# for i in range(len(a)):
#     print(a[i])

# for循环的嵌套
# a=[[1,2,3],[4,5,6]]
# for i in a:
#     for j in i:
#      print(j)
# b=[{'name':"kk","pwd":"123456"},{'name':"ss","pwd":'456789'}]
# for i in b:
#     for j in i:
#         print(i.get(j))
'''
# 用for循环实现用户登录
t_user =[{'name':"kk","pwd":"123456",'sex':'男'},{'name':"ss","pwd":'456789'}]
user=input('输入账户:')
pwd=input("输入密码:")
a=1
for i in t_user:
    if i.get('name')==user and i.get('pwd')==pwd :
     print('欢迎登陆{}'.format(i.get('name') ) )
     break
    elif a==len(t_user):
      print('登陆失败')
    a=a+1
 '''
# t_user =[{'name':"kk","pwd":"123456",'sex':'男'},{'name':"ss","pwd":'456789'}]
#作业,输入账户密码,如b中存在,那就注册失败,如果没有那就添加到t_user, 
t_user =[{'name':"kk","pwd":"123456",'sex':'男'},{'name':"ss","pwd":'456789'}]
user=input("输入账户")
pwd=input('输入密码')
a=1
for i in t_user:
  if user==i.get('name'):
    print('注册失败,账户已存在')
  elif len(t_user)==a:
   t_user.append({'name':user,'pwd':pwd})
   break
  a=a+1

print(t_user)