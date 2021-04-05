# 5-7 喜欢的水果

# 喜欢的水果列表
favorite_fruits = ["pear", "apple", "banana"]
# 所有水果
all_fruits = ["strawberry", "apple", "pear", "orange", "banana"]

# 检测水果在不在列表里，如果在，就打印一条消息
for fruits in favorite_fruits:
	if fruits in all_fruits:
		print("You really like " + fruits + ".")
