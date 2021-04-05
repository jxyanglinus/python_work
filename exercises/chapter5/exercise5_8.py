# 5-8 以特殊的方式和管理员打招呼
users = ['tom', 'linus', 'admin', 'anna', 'john']

for user in users:
	if user == 'admin':
		print("Hello, " + user.title() + ", would you like to see a status report?")
	else:
		print("Hello, " + user.title() + ", thank you for logging in again.")
