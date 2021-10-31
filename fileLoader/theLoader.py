import os


class fileLoader(object):
    def __init__(self, path):
        self.path = os.path.join(path)

# the two self get fun only read the file in target folder
    def readNames(self):
        self.ergodicReadNameFun(self.path)

    def getNames(self):
        return self.ergodicGetFun(self.path)

    @staticmethod
    def readTempCatalogue():
        path = os.getcwd()
        print(os.listdir(path))

    @staticmethod
    def isFile(file: str):
        # judge a item is a file or a folder
        for aChar in range(len(file) - 1, -1, 1):
            if aChar == ".":
                return True
            else:
                return False

    @staticmethod
    def ergodicGetFun(path, readAll=False):
        # if you want to read all the files in the sub dir turn the para to ture
        obj = []
        try:
            for root, dirs, files in os.walk(path):
                if (root != path) | readAll:
                    break
                for file in files:
                    obj.append(os.path.join(root,file))
        except:
            print(path + "is not found, please check its validation")
        # print(obj)
        return obj

    @staticmethod
    def ergodicReadNameFun(path, readAll=False):
        # read all the sub files!
        # the path preferred to be absolute path
        # this fun would list the subFile of the path
        try:
            for root, dirs, files in os.walk(path):
                if (root != path) | readAll:
                    break

                for file in files:
                    # 获取文件所属目录
                    print(root)
                    # 获取文件路径
                    print(os.path.join(root, file))

                for dir in dirs:
                    # 获取目录的名称
                    print(dir)
                    # 获取目录的路径
                    print(os.path.join(root, dir))
        except:
            print(path + "is not found, please check its validation")
