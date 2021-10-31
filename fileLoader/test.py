from theLoader import *


def test():
    f = fileLoader("../")
    # f.readNames()
    f.ergodicGetFun(f.path)
    # path = os.getcwd()
    # print(os.walk(f.path)[0])
    # print(os.listdir(f.path))
test()
