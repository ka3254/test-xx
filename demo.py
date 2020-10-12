# print('你好'+"带我玩"*3,end="111")
# print(123)
# print(2.333)
"""
print((2+2-1*1/0.5)*2)
print(True,False)
print(1>3)
print(1<3)
print(1==2 or 1<3)
print(1==2 and 1<3)
print(None)
print(())
print([])
print({})"""

# name='张三' 
# print(name)

# #运算输出
# res= (1+2+4+5*2/(4*2))%3
# print(res)

#获取内容并切换成小数进行运算
# a=input("输入:")
# b=input("输入2")
# d=int(input("输入3"))
# print(float(a)+float(b)+d)
# c=type(b)
# print(c)

#获取字段长度
# a=len("dasdadsdasd")
# print(a)

#判断输入字符串是奇数还是偶数
# print("True为奇,False为偶")
# a=len(input("请输入"))
# c=int(a)%2
# print(c>0)
''' 元组
# 元组意义在于少写变量 
# 变量会占用内存越多占用的内测就越多
b=('xx','yy')
#元组内包涵元组为2维元组,套几层,为几维元组
a=(1,2,3,4,"das",True,None,b)
# print(a)
# # 下标是计算机自动给值的编号,计算机技术从0开始,取值直接元组[值下标]
# print(a[5])
# #多层元组取值方式为下标依次深入
# print(a[-1][1])
# print( a.index(3))
# #多层元组使用方法需要先定位到该元组再使用
# print(a[-1].index('xx'))
# print(a.count("das"))
#切片 左闭右开(包括左标值,不包括右标值)
print(a[0:3])
'''

# 数组
b=('x','y')
a=[1,2,3,4,"das",True,None,b,1]
print(a)
# 数组修改例:
# n=int(input('输入'))

# a.append(n)
#a.insert(0,值)也可直接插入数据,但是因为a是嵌套数组,所以需要指定目标组,则a.insert(a[0],值)才能成功
# a.insert(0,n)

# print( a.pop(5))
# #extend方法是将对象数组的内容插入到目标数组的后端
# #拼接输出的方法也可以达到输出效果 print(a+c)
# c=['xx','yy']
# a.extend(c)
# print(a)

d=[2,3,4,6,5]
#sort是按从小到大排序,且针对于有大小关系的内容
# d.sort(reverse=True)为从大到小倒置
# d.sort()
# clear为删除数组中的内容
# d.clear()
# remove 方法的括号中是删除的是值,不是下标
# d.remove(2)
# reverse方法单独使用仅仅是将数组本身的顺序倒置,并不会按大小倒序
d.reverse()
print(d) 

