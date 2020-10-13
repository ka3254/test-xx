# if 条件语句
'''
a=int(input('输入年龄'))
if a >= 18:
    print('成年人')
else:
    print('未成年人')
# >< >= <= ==  !=
# a=len(input('请输入'))
# if a>6:
#     print('输入合格')
# else:
#     print('不合规')
'''

'''
# in 判断某个字符是否在另外一个字符串中
t='tadozppfa'
y= 'dozp'
if y in t:
    print('y存在于t')
else:
    print('不存在')
'''
'''
# 多条件 and并发才为满足  or 触发一个即为满足
# 满足长度为3,且名字为大雁塔
name = input('请输入')
if name=='大雁塔'and len(name)==3:
    print('输入正确')
else:
    print('输入错误')
'''
'''
# if的嵌套
name=input()
if len(name)==3:
    if name=='大雁塔':
        print('正确')
    else:
        print('错误')
else:
    print('错误')

'''
'''
# 多条件
a=int(input('输入年龄'))
if a>18:
    print('成年人')
elif a>16:
        print('青年人')
elif a>14:
            print('少年')
else:
    print('小孩')            
'''
# 输入一个账号+密码,账号长度>5,<8,
# 账号为张三,密码为123456直接登陆成功,否则失败
uid=input('输入账户名')
pwd=input('输入密码')
if uid=='张三' and pwd=='123456':
    print('登陆成功')
else:
    if len(uid)<5:
        print('账户过短')

    elif len(uid)>8:
           print('账户过长')
    elif pwd=='123456':
                print('账户错误')
    else:
                print('密码错误')
