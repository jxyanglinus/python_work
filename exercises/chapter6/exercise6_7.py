# 6-7 人

# 人的信息
friend_1 = {'first_name': 'linus', 'last_name': 'yang', 'age': 13, 'city': 'luzhou'}
friend_2 = {'first_name': 'elli', 'last_name': 'du', 'age': 12, 'city': 'luzhou'}
friend_3 = {'first_name': 'tim', 'last_name': 'cook', 'age': 61, 'city': 'new york'}
people = [friend_1, friend_2, friend_3]  # 存储在一个列表中

# 打印消息
for info in people:
	full_name = info['first_name'].title() + " " + info['last_name'].title()
	print("= " * 20)
	print("Name: " + full_name)
	print("Age: " + str(info['age']))
	print("Lives: " + info['city'].title())
