import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize as optim

class LinearFiter(object):
    def __init__(self):
        pass

    def linearFun(self,x,A,B):
        return x*A+B