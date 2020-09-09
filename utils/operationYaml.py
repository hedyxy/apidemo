import yaml
from common.public import filePath

class OperationYmal:
    def readYaml(self):
        with open(filePath(),'r',encoding='utf-8') as f:
            return list(yaml.safe_load_all(f))


    def dicYaml(self,fileDir='config',fileName='books.yaml'):
        with open(filePath(fileDir=fileDir,filename=fileName),'r',encoding='utf-8') as f:
            return yaml.safe_load(f)

if __name__ == '__main__':
    obj = OperationYmal()
    # print(obj.readYaml())
    # for item in obj.readYaml():
    #     print(item)
    print(obj.dicYaml()['book_002'])