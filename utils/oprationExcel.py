import xlrd
from common.public import filePath
from utils.operationYaml import OperationYmal


class ExcelVarles(object):
    caseID = 0
    des = 1
    url = 2
    method = 3
    data = 4
    expect = 5

    @property
    def getCaseID(self):

        return self.caseID

    @property
    def description(self):
        return self.des

    @property
    def getUrl(self):
        return self.url

    @property
    def getMethod(self):
        return self.method

    @property
    def getData(self):
        return self.data

    @property
    def getExpect(self):
        return self.expect


class OprationExcel(OperationYmal):


    def getSheet(self):
        book = xlrd.open_workbook(filePath('data','books.xlsx'))
        return book.sheet_by_index(0)

    @property
    def getRows(self):
        '''
        获取总行数
        :return:
        '''
        return self.getSheet().nrows

    @property
    def getCols(self):
        '''
        获取总列数
        :return:
        '''
        return self.getSheet().ncols

    def getValue(self,row,col):
        '''

        :param row: 行
        :param col: 列
        :return: 传入行、列获取对应的值
        '''
        return self.getSheet().cell_value(row,col)

    def getCaseID(self,row):
        '''获取caseID，只需要传入行即可'''
        return self.getValue(row=row,col=ExcelVarles().getCaseID)

    def getUrl(self,row):
        return self.getValue(row=row,col=ExcelVarles().getUrl)

    def getMethod(self,row):
        return self.getValue(row=row,col=ExcelVarles().getMethod)

    def getData(self,row):
        return self.getValue(row=row,col=ExcelVarles().getData)

    def getJson(self,row):
        return self.dicYaml()[self.getData(row=row)]

    def getExpect(self,row):
        return self.getValue(row=row,col=ExcelVarles().getExpect)

    def getExcelDatas(self):
        datas = list()
        title = self.getSheet().row_values(0)
        for item in self.getRows:
            row_values = self.getSheet().row_values(item)[0]
            datas.append(dict(zip(title,row_values)))#把值搞成字典
        return datas

    def runs(self):
        '''获取到可执行的测试用例'''
        run_list=[]
        for item in self.getExcelDatas:
            isRun=item[ExcelVarles.isRun]
            if isRun=='y':run_list.append(item)
            else:pass
        return run_list

    def params(self):
        '''对请求参数为空的处理'''
        for item in self.runs():
            params = item[ExcelVarles.params]
            print(params)


if __name__ == '__main__':
    obj = OprationExcel()

    # print(obj.getCaseID(row=2))
    # print(obj.getMethod(row=2))
    # print(obj.getJson(row=4))
    obj.params()