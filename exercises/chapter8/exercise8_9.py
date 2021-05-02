# 8-9 魔术师

def show_magicians(magicians):
	"""打印所有魔术师的名称"""
	for magician in magicians:
		print(magician.title())


magicians_list = ['joe', 'jeff', 'tom', 'elli']

show_magicians(magicians_list)
