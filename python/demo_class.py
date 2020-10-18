#类
"""
class Persen():
    #成员变量 类中的变量
 name='明'
 age= 18
 sex='男'
 #成员方法,类中的方法
 def eat(self,sth):
     #调用类中变量
   print(self.name+'吃了{}'.format(sth))

 def lunch(self):
  self.eat('午饭')
#调用类:实例化类:p为实例化对象,或者类的把柄
p=Persen()
print(p.name)
p.lunch()#self不需要传参

"""
'''
#类的继承
# 子类Son父类Dad
class Dad():
 money='1e'
  def make_money(self):
   print('他爸爸的小目标')

class Son(Dad):
    name='son'
    money='-10e'
    def make_money(self):
      print('小王创业了')
s=Son()
print(s.money)
s.make_money()
'''

class Cat():
    #构造方法 固定方法,实例化的时候运行
 def __init__(self,mx):
     self.name=mx
# 实例化的时候需要给出构造方法的参数,必须加
c=Cat("tomcat")
print(c.name)