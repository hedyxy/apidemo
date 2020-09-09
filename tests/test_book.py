from base.method import Requests
from utils.operationYaml import OperationYmal
from utils.oprationExcel import OprationExcel
import pytest
import json

class TestBook(object):

    excel=OprationExcel()
    obj = Requests()

    def result(self,r,row):
        assert r.status_code==200
        assert self.excel.getExpect(row=1) in json.dumps(r.json(),ensure_ascii=False)

    def test_book_001(self):
        '''获取所有书籍信息'''
        r=self.obj.get(url=self.excel.getUrl(row=1))
        self.result(r=r,row=1)

if __name__ == '__main__':
    pytest.main("-s","-v","test_book.py")
