def grabTree(filename):
	'''
	并在需要的时候将其读取出来
	'''
	import pickle
	fr = open(filename)
	return pickle.load(fr)
	