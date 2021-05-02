# 8-10 了不起的魔术师

def show_magicians(magicians):
	"""打印所有魔术师的名称"""
	for magician in magicians:
		print(magician.title())


def make_great(magicians):
	"""在魔术师名字中加入 'the Great' 字样"""
	length = len(magicians)
	index = 0
	while index < length:
		magicians[index] = 'the Great ' + magicians[index].title()
		index += 1


magicians_list = ['joe', 'jeff', 'tom', 'elli']

make_great(magicians_list)
show_magicians(magicians_list)
