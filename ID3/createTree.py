from chooseBestFeatureToSplit import chooseBestFeatureToSplit

def createTree(dataSet, labels):
	'''
		创建决策树的函数
	dataSet 需要被分类的数据集
	lables  特征
	'''
	classList = [example[-1] for example in dataSet] 		# 训练数据的类标签
	if classList.count(classList[0]) == len(classList): 	# 若类别 == 整个类别标签长度， 则类别缀有唯一一个
		return classList[0]
	if len(dataSet[0]) == 1:								# 如果数据集没有特征值，返回类别数据最多的类别
		return majorityCnt(classList)
	bestFeat = chooseBestFeatureToSplit(dataSet)			# 选出数据集中最佳的划分自己特征
	bestFeatLable = lables(bestFeat)						# 将此特征名作为树根节点
	myTree = {bestFeatLabel:{}}								# 初始赋值决策树
    del(labels[bestFeat])									# 删除已选择的特征名
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
        
    return myTree