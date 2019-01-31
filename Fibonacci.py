def fibonaci(n):
	if n == 1 or n == 2:
		return 1
	elif (n-2)>0:
		return fibonaci(n-1) + fibonaci(n-2)
	else:
		return 0

num = int(input("请输入截止月数："))
if num < 0:
	print("输入有误")
result = fibonaci(num)
print("%d 个月共有 %d 对兔子" % (num,result))
