# 8-8 用户的专辑

def make_album(singer, album_name, songs_num):
	"""返回专辑的信息"""
	info = {
		'singer': singer.title(),
		'album_name': album_name.title(),
		'songs_num': songs_num
	}

	return info


def main():
	"""主方法"""
	infos = []  # 存储专辑的信息

	print("现在，让我们来录入一些专辑的信息!")
	print(" * 提示：输入'q'可在任意时候退出信息的录入")

	while True:
		"""录入信息"""
		singer = input("输入歌手的名字:")
		if singer == 'q':
			break

		album = input("输入专辑的名字:")
		if album == 'q':
			break

		songs = input("输入这个专辑的歌的数量:")
		if songs == 'q':
			break
		songs = int(songs)

		infos.append(make_album(singer, album, songs))
		print("+++++++添加成功+++++++")

	print('\n')
	for info in infos:  # 输出所有专辑信息
		for key, val in info.items():
			if key == 'singer':
				print("歌手: " + val)
			elif key == 'album_name':
				print("专辑名称: " + val)
			elif key == 'songs_num':
				print("歌曲数量: " + str(val))
		print('=' * 20)


if __name__ == '__main__':
	main()
