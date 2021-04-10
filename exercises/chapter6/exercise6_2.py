# 6-2 喜欢的数字
favorite_numbers = {
	'eric': 30,
	'tom': 233,
	'linus': 3.14,
	'anna': 777,
	'jack': 456
	}  # 喜欢的数字

print("Their favorite numbers:")
for k, v in favorite_numbers.items():
	print(str(k).title() + ': ' + str(v))
