def storeTree(inputTree, filename):
	'''
	决策树的存储
	pickle序列化对象， 可以在磁盘上保存对象
	'''
	import pickle
	fw = open(filename, 'w')
	pickle.dump(inputTree, fw)
	fs.close()