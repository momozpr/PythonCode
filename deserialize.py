#使用pickle模块从文件中重构python对象

import pprint,pickle

with open("data.pkl",'rb') as pkl_file:
	data1 = pickle.load(pkl_file)
	pprint.pprint(data1)
	data2 = pickle.load(pkl_file)
	pprint.pprint(data2)
# 递归数据结构有指向原数据源的引用来表示，形式为<Recursion on typename with id=number>

pkl_file.closed
