# 7-10 梦想的旅游胜地

responses = {}  # 存储信息的字典

"""调查"""
while True:
	name = input("你的名字是什么:")
	place = input("你最想去哪里旅行:")
	responses[name] = place  # 存入字典

	report = input("你想继续进行调查吗:")
	if report == 'no':
		break
	else:
		continue

"""打印调查结果"""
print('-' * 50)  # 分割
for name, place in responses.items():
	print(name + " 想要去 " + place)
