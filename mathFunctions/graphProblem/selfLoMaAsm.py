from fileLoader.theLoader import *
from mathFunctions.graphProblem.ZaMatrix import *


class selfLMaAsm(fileLoader):
    def __init__(self, path):
        fileLoader.__init__(self, path)
        self.matrix = []
        self.readTheMatirx()


    def readTheMatirx(self):
        self.matrix = []
        for i in self.getNames():
            # print(i)
            self.matrix.append(Matrix(i))
