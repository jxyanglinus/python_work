# 5-10 检查用户名
current_users = ['tom', 'linus', 'admin', 'anna', 'john']  # 已有用户
new_users = ['anna', 'jack', 'tom', 'eric', 'tim']  # 新增用户

for new_user in new_users:
	# 注册新用户时，检测这个名称是否已经存在；比较时不区分大小写
	lower_name = [name.lower() for name in current_users]  # 先将名字转换为小写
	if new_user.lower() in lower_name:
		print(new_user.title() + "已被使用!请换一个名称!")
	else:
		print(new_user.title() + "注册成功!")
