# 6-9 喜欢的地方

favorite_places = {  # 存储喜欢的地方的字典
	'linus': ['luzhou', 'wuhan', 'chongqing'],
	'tom': ['shanghai', 'guangzhou'],
	'jack': ['shanxi', 'zhejiang', 'fujian'],
}

# 打印消息
for people, places in favorite_places.items():
	print(people.title() + " likes these places:")
	for place in places:
		print('\t' + place.title())
