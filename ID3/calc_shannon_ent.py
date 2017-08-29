from math import log

# 计算给定数据集的香农熵
def calcShannonEnt(dataset):
	numEntries = len(dataset)
	labelCounts = {}
	for featVec in dataset:
		currentLable = featVec[-1]
		if currentLable not in labelCounts.key():
			labelCoutns[currentLable] = 1
		labelCoutns[currentLable] += 1


	shannonEnt = 0.0
	for key in labelCounts:
		prob = float(labelCounts[key]) / numEntries
		shannonEnt -= prob * log(prob, 2)

	return shannonEnt