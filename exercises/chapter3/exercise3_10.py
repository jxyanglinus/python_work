# 3-10 尝试使用各个函数

people = ["Tom", "Linus", "Rick", "June", "Anna"]

print("一共有" + str(len(people)) + "个人")
print("他们分别是: ")
for name in people:
    print('\t' + name.title())

print("我想，我忘记了一些人")
people.append("Jack")
people.insert(0, "Sam")

print("现在，一共有" + str(len(people)) + "个人")
print("他们分别是: ")
for name in people:
    print('\t' + name.title())

print("按名字首字母排列是:")
people.sort()
for name in people:
    print('\t' + name.title())

print("反过来排序的话: ")
people.sort(reverse=True)
for name in people:
    print('\t' + name.title())
