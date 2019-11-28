#coding:utf-8


##xls文档的读取与写入

import xlrd


def xls_read(path,sheet):
    # 打开文件
    data = xlrd.open_workbook(path)
    table = data.sheet_by_name(sheet)  # 通过名称获取表单
    nrows = table.nrows
    nclos = table.ncols
    for i in range(nrows):
        print table.row_values(i)



if __name__ ==  "__main__":
    xls_read(r'C:\Users\user\Desktop\1111.xls',r"Sheet1")



