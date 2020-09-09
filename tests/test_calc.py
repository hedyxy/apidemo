import pytest
@pytest.mark.parametrize('a,b',(1,2))
def calc(a,b):
    r=a+b
    assert r in 3

if __name__ == '__main__':
    # pytest.main(["-s", "v", "test_calc.py"])
    pytest.main(["-s", "v", "/Users/hedy/Desktop/apiFramework/tests/test_calc.py", "--allurdir", "./report/result"])
    import subprocess

    subprocess.call('allure generate report/result/ -o report/html --clean', shell=True)
    subprocess.call('allure open -h 127.0.0.1 -p 8088 .report/html', shell=True)