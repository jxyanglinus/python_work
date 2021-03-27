# 3-9 晚餐嘉宾
names = ["张三", "李四", "王五"]

print("你好，" + names[0] + "，你要来一起吃饭吗?")
print("你好，" + names[1] + "，你要来一起吃饭吗?")
print("你好，" + names[2] + "，你要来一起吃饭吗?")

# 不能来的嘉宾
print("\n*" + names[1] + "无法参加！\n")

# 将不能来的嘉宾替换掉
names[1] = "罗翔"

# 再次发出邀请

print("你好，" + names[0] + "，你要来一起吃饭吗?")
print("你好，" + names[1] + "，你要来一起吃饭吗?")
print("你好，" + names[2] + "，你要来一起吃饭吗?")

# 找到了更大的桌子
print("\n*我找到了一张更大的桌子!\n")

# 添加嘉宾
names.insert(0, "小明")
names.insert(2, "小红")
names.append("小军")


print("你好，" + names[0] + "，你要来一起吃饭吗?")
print("你好，" + names[1] + "，你要来一起吃饭吗?")
print("你好，" + names[2] + "，你要来一起吃饭吗?")
print("你好，" + names[3] + "，你要来一起吃饭吗?")
print("你好，" + names[4] + "，你要来一起吃饭吗?")
print("你好，" + names[5] + "，你要来一起吃饭吗?")

# 一共有多少嘉宾参加了宴席
print("现在有 " + str(len(names)) + " 名嘉宾参加了宴席!")
