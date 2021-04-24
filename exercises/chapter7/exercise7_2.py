# 7-2 餐厅订位

people = input("你好!请问有多少人用餐呢: ")
people = int(people)

if people > 8:
	print("对不起,没有空桌了")
else:
	print("还有空桌,订位成功!")
