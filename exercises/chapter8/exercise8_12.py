# 8-12 三明治

def make_sandwich(*toppings):
	"""制作三明治"""
	for topping in toppings:
		print(' - Adding ' + topping)
	print("Completed!")


make_sandwich('meat', 'salad', 'egg', 'carrot')
