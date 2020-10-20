import xlrd
# (参数依次为excel表名,sheet名,是否跳过首行,默认为跳过)
def read_excel(excel_path,sheet_name,skip_first=True):
    results=[]
    # 打开excel_path表格
    datas =xlrd.open_workbook(excel_path)
     # 打开sheet_name页面
    table= datas.sheet_by_name(sheet_name)
    if skip_first==True:
        start_row=1
    else:
        start_row=0
        # 循环读取每行内容
    for row in range(start_row,table.nrows):
        results.append(table.row_values(row))

    return results
# 根据实际表格修改
# print(read_excel('data.xlsx',"Sheet1"))
