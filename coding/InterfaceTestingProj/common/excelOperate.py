import os
import xlrd
from xlutils.copy import copy
def readExcelOperate(sheet_value,row_value,col_value):
    #获取当前文件夹父目录的绝对路径
    BASE_DIR=os.path.dirname(os.path.dirname(__file__))
    print(BASE_DIR)
    #合并当前路径
    fileName=os.path.join(BASE_DIR,"testData/",'interface.xlsx')
    #打开工作簿
    data=xlrd.open_workbook(fileName)
    #选择工作页
    sheet=data.sheet_by_index(sheet_value)
    #读取行列
    dataValue=sheet.row(row_value)[col_value].value
    return dataValue
def writeExcelOperate(sheet_value,row_value,col_value,content):
    #获取当前文件夹父目录的绝对路径
    BASE_DIR=os.path.dirname(os.path.dirname(__file__))
    print(BASE_DIR)
    #合并当前路径
    fileName=os.path.join(BASE_DIR,"testData/",'interface.xlsx')
    #打开工作簿
    data=xlrd.open_workbook(fileName)
    #利用原工作簿创建新工作簿
    newData=copy(data)
    #创建工作页
    newWS=newData.get_sheet(0)
    #写入行列中数据
    newWS.write(1,3,content)
    #保存文档
    newWS.save(fileName)



