from calc_shannon_ent import calcShannonEnt
from splitDataSet_function import splitDataSet

# 选择最好的数据集划分方式
def chooseBestFeatureToSplit(dataSet):
	'''
	函数将数据集按照信息增益最大的标准分类， 返回一个最好的分类索引
	:param dataSet: 需要分类属性的数据集
	'''
	numFeatures = len(dataSet[0]) - 1 # 计算给定数据集的特征属性数
	baseEntropy = calcShannonEnt(dataSet) # 计算给定数据集的香农熵
	bestInfoGain = 0.0
	bestFeature = -1 # 最好的特征属性序列
	for i in range(numFeatures):
		featList = [example[i] for example in dataSet] # 获取特征属性的列表
		uniqueVals = set(featList) # 特征属性列表的 唯一值
		newEntroy = 0.0
		for value in uniqueVals:
			subDataSet = splitDataSet(dataSet, i, value)
			prob = len(subDataSet) / float(len(dataSet))
			newEntroy += prop * calcShannonEnt(subDataSet)
		infoGain = baseEntropy - newEntroy 		# 计算信息增益
		if (infoGain > bestInfoGain):
			bestInfoGain = infoGain
			bestFeature = i
	return bestFeature
