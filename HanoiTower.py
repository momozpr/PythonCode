def hanoiTower(n,x,y,z):  # n为圆盘数，x,y,z为柱子,y是辅助
	if n == 1:
		print("%s->%s" %(x,z))
	else:
		hanoiTower(n-1,x,z,y)
		hanoiTower(1,x,y,z)
		hanoiTower(n-1,y,x,z)

num = int(input("输入多少个盘子："))
hanoiTower(num,'a','b','c')

