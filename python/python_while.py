# a=10
# while a>0:
#      print(a)
#      a=a-1
'''
# list[80,60,59,29,99],判断成绩是否合格,把不合格的成绩打印出来
cj=[80,60,59,29,99]
a=0 #成绩的下标
while a<len(cj):
    if cj[a]<60:
     print("不合格,成绩为{}".format(cj[a]))
    a=a+1
'''

#一共60s,红 35 绿 10 黄5,分别打印
a=0
while a<60:
    if a<5:
        print('黄灯{}'.format(a+1))
    elif a<25:
      print('绿灯{}'.format(a-4))
    else:
        print('红灯{}'.format(a-24))
    a=a+1
