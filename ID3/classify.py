def classify(inputTree, featLables, testVec):
	'''
	使用决策树进行分类
	inputTree  训练好的决策树
	featLbales 构建数的类别标签向量（用于确定特征在数据集中的位置）
	testVec	   测试数据，判断属于哪个类别
	'''
	firstStr = inputTree.keys()[0]		# firstStr存放决策树的根节点
	secondDit = inputTree[firstStr] 	# secondDit值为除根节点名称外的值
	featIndex = featLbels.index(firstStr)	#index方法查找当前列表中第一个匹配firstStr变量的元素的索引

	key = testVec[featIndex]	# 测试数据对应根节点下的取值
	valueOfFeat = secondDict[key]	# 判断valueOfFeat的类型，Dict类型，递归查找
	if isinstance(valueOfFeat, dict):
		clssLabel = classify(valueOfFeat, featLables, testVec)
	else: classLabel = valueOfFeat