import xlrd, xlwt, openpyxl
import pandas as pd
import numpy as np
import sys




class Matrix(object):
    def __init__(self, path, sheetId=0):
        self.path = path
        self.obj = self.readExcel(self.path, sheetId)

    def disp(self):
        print(self.obj)

    def reRead(self):
        self.obj = self.readExcel(self.path)

    @staticmethod
    def readExcel(path, sheetId=0, haveHeader=False):
        typeName=path[-4:]
        if (typeName =="xlsx") | (typeName==".xls"):
            try:
                obj = pd.read_excel(path, header=0, index_col=0, sheet_name=sheetId)
                # print(obj)
                head = np.array(obj.columns)
                obj = obj.values
                if haveHeader:
                    obj = np.row_stack((head, obj))
                return obj
            except :
                sys.exit("fail to fetch, please check the file exist or not.")
        else:
            sys.exit("invalid filetype, please check your path.")

# 从网络cut的
def read(file):
    wb = xlrd.open_workbook(filename=file)#打开文件
    sheet = wb.sheet_by_index(0)#通过索引获取表格
    rows = sheet.nrows # 获取行数
    all_content = []        #存放读取的数据
    for j in range(0, 2):       #取第1~第2列对的数据
        temp = []
        for i in range(1,rows) :
            cell = sheet.cell_value(i, j)   #获取数据
            temp.append(cell)
        all_content.append(temp)    #按列添加到结果集中
        temp = []
    return np.array(all_content)    #返回读取的数据


def loaddataset(filename):
    fp = open(filename)

    # 存放数据
    dataset = []

    # 存放标签
    labelset = []
    for i in fp.readlines():
        a = i.strip().split()

        # 每个数据行的最后一个是标签
        dataset.append([float(j) for j in a[:len(a) - 1]])
        labelset.append(int(float(a[-1])))
    return dataset, labelset

