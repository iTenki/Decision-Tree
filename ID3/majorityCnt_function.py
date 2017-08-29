import operator

def majorityCnt(classList):
	'''
	多数表决的方法决定叶子节点的分类
	所有特征都用完时，以数据集中类别数量最多的类别作为最终类型
	'''
	classCount = {}
	for vote in classList:
		if vote not in classCount.key():
			classCount[vote] = 0
		classCount[vote] += 1
	# 遍历结束后，次数value值从大到小进行排列
	sortedClassCount = sorted(classList.iteritems(), key = operator.itemgetter(1), reverse = True)  # 利用operator操作键排序字典
	return sortedClassCount[0][0]	# 返回数量最多的类别