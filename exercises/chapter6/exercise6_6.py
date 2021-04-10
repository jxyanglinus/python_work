# 6-6 调查

# 已经参加调查的人
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

# 所有需要参加的人
participants = ['jen', 'edward', 'phil', 'june', 'sarah', 'linus', 'galaxy']

for participant in participants:
	if participant in favorite_languages:
		# 如果这个人已经参与过了，就打印一条消息表示感谢
		print(participant.title() + ". Thank you for your participation.")
	else:
		# 如果没有，就打印一条消息提示他尽快参与
		print(participant.title() + ". Please take part in our survey.")
