# 类定义
class people:
	#定义基本属性
	name = ""
	age = 0

	#定义私有属性
	__weight = 0

	#定义构造函数
	"""docstring for people"""
	def __init__(self, n, a, w):
		self.name = n
		self.age = a
		self.__weight = w

	#定义方法
	def speak(self): #第一个参数必须是self
		print("%s 说：我%d岁。" %(self.name,self.age))

#单继承示例
class student(people):
	grade = ''
	def __init__(self,n,a,w,g):
		people.__init__(self,n,a,w)
		self.grade = g

	#重写父类的方法
	def speak(self):
		print("%s 说：我%d 岁了，我在读%d年级"%(self.name,self.age,self.grade))

#类
class speaker():
	topic = ''
	name = ''

	"""docstring for speaker"""
	def __init__(self, n,t):
		self.name = n
		self.topic = t

	def speak(self):
		print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))

# 多重继承
class sample(speaker,student):
	a = ''
	def __init__(self,n,a,w,g,t):
		student.__init__(self,n,a,w,g)
		speaker.__init__(self,n,t)

test = sample("Tim",25,80,4,"Python")
test.speak()   # 方法名相同，默认使用前面的父类的方法