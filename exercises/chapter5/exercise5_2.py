# 5-2 更多条件测试

# 检测字符串
car = "Audi"

print(car == "audi")
print(car.lower() == "audi")

print('\n')

# 检测数字
val_1 = 399
val_2 = 520

print(val_1 == val_2)
print(val_1 != val_2)
print(val_1 > val_2)
print(val_1 < val_2)
print(val_1 >= val_2)
print(val_1 <= val_2)

print('\n')

# 关键词and和or
age_1 = 14
age_2 = 21

print(age_1 > 18 and age_2 > 18)
print(age_1 > 18 or age_2 > 18)

print('\n')

# 某个值在列表中吗?
foods = ['ice-cream', 'hamburger', 'strawberry']
if 'ice-cream' in foods:
    print("Sorry, we don't have ice-cream.")

print('\n')

# 某个值不包含在列表中吗?
names = ['anna', 'tom', 'mike']
if 'jack' not in names:
    print("Hey, where is Jack?")
