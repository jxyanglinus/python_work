# 7-9 五香烟熏牛肉卖完了
sandwich_orders = ['pastrami', '芝士三明治', 'pastrami', '鸡肉三明治', 'pastrami', '培根三明治', '肉松三明治']
finished_sandwich = []

print("* 五香烟熏牛肉卖完了")
while 'pastrami' in sandwich_orders:  # 从列表中移除所有五香烟熏牛肉三明治
	sandwich_orders.remove('pastrami')  # 因为直接用中文的’五香烟熏牛肉‘要出问题，所以用英文

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print("正在制作 " + current_sandwich + " ...")
	finished_sandwich.append(current_sandwich)

print("所有三明治均制作完成!")
