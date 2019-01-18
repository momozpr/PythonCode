a = 4

def print_func1():
	a = 17
	print("in print_func1 a = ",a)
def print_func2():
	print("in print_func2 a = ",a)

sum = lambda args1,args2:args1+args2;

print("Value of total:",sum(10,20))
print("Value of total:",sum(20,20))

print_func1()     #局部
print_func2()     #全局
print("a = ",a)   #全局

def parrot(voltage,state="a stiff",action="voom",type="Norwegian Blue"):
	print("-- This parrot wouldn't",action,end=" ")
	print("-- This parrot wouldn't",voltage,end=" ")
	print("-- This parrot wouldn't",type,end=" ")
	print("-- This parrot wouldn't",state,end=" ")


parrot(1000)
parrot(voltage=1000)
parrot(voltage=100000,action="VOOOOOM")
parrot(action="VOOOM",voltage="asd")
parrot("a million","bereft of life")
parrot('a thousand',state='push it')