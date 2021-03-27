# 3-7 缩减名单
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

# 新桌子暂时送不到
print("\n*新的桌子暂时无法送到!\n")
print("*只能邀请两位嘉宾!\n")

# 删除嘉宾
print("很抱歉，" + names.pop() + "，无法邀请你来参加宴会!")
print("很抱歉，" + names.pop() + "，无法邀请你来参加宴会!")
print("很抱歉，" + names.pop() + "，无法邀请你来参加宴会!")
print("很抱歉，" + names.pop() + "，无法邀请你来参加宴会!")

# 告诉另两位嘉宾他们仍在受邀人之列
print("嘿！" + names[0] + "，你仍然在受邀请的人的行列中!")
print("嘿！" + names[1] + "，你仍然在受邀请的人的行列中!")

# 删除最后两位嘉宾
del names[1]
del names[0]

# 确认列表为空
print(names)
