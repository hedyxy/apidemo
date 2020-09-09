import pytest
from base.method import Requests
from utils.operationYaml import OperationYmal
import json


obj = Requests()
objyaml = OperationYmal()

@pytest.mark.parametrize('datas',objyaml.readYaml())
def test_login(datas):
    r = obj.post(url=datas['url'],
                 json=datas['data'])
    assert datas['expect'] in json.dumps(r.json(),ensure_ascii=False)



if __name__ == '__main__':
    pytest.main(["-s","v","test_login.py","--allurdir","./report/result"])
    import subprocess
    subprocess.call('allure generate report/result/ -o report/html --clean',shell=True)
    subprocess.call('allure open -h 127.0.0.1 -p 8088 .report/html',shell=True)