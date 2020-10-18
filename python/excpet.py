res = (1,2,3,4)
try:
 res[30]
 print('试着运行的')
except Exception as e:
    print(e)
    print('报错了运行')
else:#可选
    print('没有报错运行的')
finally:#可选
    print('无论报没报错都执行的')