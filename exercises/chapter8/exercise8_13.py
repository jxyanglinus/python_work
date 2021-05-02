# 8-13 用户简介

def build_profile(first, last, **user_info):
	"""创建一个字典，其中包含我们知道的有关用户的一切"""
	profile = {
		'first_name': first.title(),
		'last_name': last.title()
	}

	for key, val in user_info.items():
		profile[key] = val

	return profile


me = build_profile('linus', 'young', age=13, school='Tianli', favorite_language='Python')
print(me)
