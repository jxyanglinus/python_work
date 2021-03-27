# 3-8 放眼世界

# 地点
places = ["Shanghai", "Beijing", "Xizang", "Shenzhen", "Wuhan"]

# 原始状态
print(places)

# 临时排序
print(sorted(places))
# # 确认列表未被修改
print(places)

# 临时排序(反向)
print(sorted(places, reverse=True))
# # 确认列表未被修改
print(places)

# 永久修改排列顺序
places.reverse()
print(places)

# 恢复排列顺序
places.reverse()
print(places)

# 按字母排列列表
places.sort()
print(places)

# 按字母排列列表(反向)
places.sort(reverse=True)
print(places)
