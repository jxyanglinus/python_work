# 7-8 熟食店

sandwich_orders = ['芝士三明治', '鸡肉三明治', '培根三明治', '肉松三明治']
finished_sandwich = []

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print("正在制作 " + current_sandwich + " ...")
	finished_sandwich.append(current_sandwich)

print("所有三明治均制作完成!")
