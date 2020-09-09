import os
# print(os.path.join())
# base_path =os.path.dirname(os.path.dirname(__file__))
# os.path.join(base_path,'data','login.yaml')

def filePath(fileDir='data',filename='login.yaml'):
    '''

    :param fileDir: 要操作的文件目录
    :param filename: 文件的名称
    :return:
    '''
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),fileDir,filename)


def writeContent(content):
    with open(filePath(filename=content),'w',encoding='utf-8') as f:
        f.write(str(content))