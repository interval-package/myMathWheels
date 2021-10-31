from bp import *

if __name__ == '__main__':
	dataset, labelset = loaddataset('time.txt')
	weight1, weight2, value1, value2 = parameter_initialization(len(dataset[0]), len(dataset[0]), 1)
	for i in range(1500):
		weight1, weight2, value1, value2 = trainning(dataset, labelset, weight1, weight2, value1, value2)
	rate = testing(dataset, labelset, weight1, weight2, value1, value2)
	print("正确率为%f"%(rate))
