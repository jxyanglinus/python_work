# 5-11 序数

# 打印1~9的序数词形式
for value in range(1, 10):
	if value == 1:
		print(str(value) + 'st')
	elif value == 2:
		print(str(value) + 'nd')
	elif value == 3:
		print(str(value) + 'rd')
	else:
		print(str(value) + 'th')
