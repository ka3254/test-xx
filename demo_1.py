a={'name':'张三','age':12}
print(a['age'])
# 取值
print(a['name'])#key不存在时是报错
print(a.get('name1'))#key不存在是返回空
#新增
a['adress']='城会玩'#key不存在就新增,存在就修改
a.update(Frinds='王二')#update写法时,key是一个变量
#取走
a.pop('age')
#通用的删除方法,可用于指点和数组
del a['name']#用于数组的时候写下标也可
print(list(a.keys()))#单获取字典a中的key名并将其数组化
print(list(a.values()))#单获取字典a中values并将其数组化
print(a)