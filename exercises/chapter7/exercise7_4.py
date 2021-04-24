# 7-4 比萨配料

print("我们将会为您制作比萨,接下来请输入你想加入的配料!")
print("* 提示:输入quit在任何时候退出")

while True:
	topping = input("请输入一个你想要的配料: ")
	if topping == 'quit':
		break
	print("好的,我们将在你的比萨中添加 " + topping)
