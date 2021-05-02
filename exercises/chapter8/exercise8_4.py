# 8-4 大号T恤

def make_shirt(size=175, text='I love Python'):
	"""制作一件T恤"""
	print("将制作一件" + str(size) + "寸的T恤。")
	print("将在这上面添加这段文字:" + text)


make_shirt()
make_shirt(155)
make_shirt(text='Manjaro')
