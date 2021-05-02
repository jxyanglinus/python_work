# 8-7 专辑

def make_album(singer, album_name, songs_num=0):
	"""返回专辑的信息"""
	info = {
		'singer': singer.title(),
		'album_name': album_name.title()
	}

	if songs_num:
		info['songs_num'] = songs_num

	return info


albums = [
	make_album('les gordon', 'la', 13),
	make_album('les gordon', 'what to do'),
	make_album('les gordon', 'visions')
]

for album in albums:  # 核对信息
	print(album)
