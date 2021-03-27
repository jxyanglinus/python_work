# 4-11 你的披萨和我的披萨
my_pizzas = ["鸡肉披萨", "火腿披萨", "水果披萨"]
friend_pizzas = my_pizzas[:]

# 给两个列表分别追加一个元素(披萨)
my_pizzas.append("烟熏牛肉披萨")
friend_pizzas.append("意式小银鱼披萨")

for pizza in my_pizzas:
    print("我喜欢" + pizza + "!")

print('\n')

for pizza in friend_pizzas:
    print("我的朋友喜欢" + pizza + "!")
