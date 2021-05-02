# 8-11 不变的魔术师

def make_great(magicians):
	"""在魔术师名字中加入 'the Great' 字样"""
	length = len(magicians)
	index = 0
	while index < length:
		magicians[index] = 'the Great ' + magicians[index].title()
		index += 1

	return magicians


def show_magicians(magicians):
	"""打印所有魔术师的名称"""
	for magician in magicians:
		print(magician.title())


magicians_list = ['joe', 'jeff', 'tom', 'elli']
changed_list = make_great(magicians_list[:])  # 存储副本
show_magicians(magicians_list)
print('-' * 20)
show_magicians(changed_list)
