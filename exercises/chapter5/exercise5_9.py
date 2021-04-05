# 5-9 处理没有用户的情景
# users = ['tom', 'linus', 'admin', 'anna', 'john']
users = []

if users:
	for user in users:
		if user == 'admin':
			print("Hello, " + user.title() + ", would you like to see a status report?")
		else:
			print("Hello, " + user.title() + ", thank you for logging in again.")
else:
	print("We need to find some users!")
