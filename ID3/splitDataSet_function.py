def splitDataSet(dataSet, axis, value):
	'''
	按照给定特征划分数据集 返回一个列表
	:param dataSet: 待划分的数据集
	:param axis: 划分数据集的特征 -- 数据的第几列
	:param value: 需要返回的特征值
	'''
	retDatasSet = []
	for featVec in dataSet:
		if featVec[axis] == value:
			reducedFeatVec = featVec[:axis]			# 获取从第0列到特征列的数据
			reducedFeatVec.extend(featVec[axis+1:]) # 获取从特征列之后的数据
			retDatasSet.append(reducedFeatVec)
	return retDatasSet