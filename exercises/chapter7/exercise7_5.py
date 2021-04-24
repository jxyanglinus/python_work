# 7-5 电影票

age = 0  # 年龄
price = 0  # 票价

print("* 根据年龄的不同,收费的标准不同 *")
while True:
	age = input("你现在多少岁: ")
	if age == 'exit':
		break
	age = int(age)
	if age < 3:
		price = 0
	elif 3 <= age < 12:
		price = 10
	elif age >= 12:
		price = 15
	print("你需要支付 " + str(price) + " 元.")
