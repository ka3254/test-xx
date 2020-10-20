'''
# import pandas as pd
# # 读取
# data=pd.read_excel('data.xlsx',sheet_name='登陆')
# # 查看所有值
# print(data)
# # 如果data的编号==1就修改为100
# data['编号'][data['编号']==1] = 100
# # 输出为xlsx格式到登陆SHEET中
# data.to_excel('data.xlsx',"登陆")
'''
from tools.excel_tools import read_excel

a=read_excel('data.xlsx',sheet_name='登陆',skip_first=False)
print(a)
