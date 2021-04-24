# 7-3 10的倍数

number = input("请输入一个数字: ")
number = int(number)

if number % 10 == 0:
	print(str(number) + "是10的倍数")
else:
	print(str(number) + "不是10的倍数")
