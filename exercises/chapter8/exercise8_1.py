# 8-1 消息

def display_message():
	"""显示一些消息"""
	messages = ['什么是函数', '怎么定义和调用函数', '实参和形参', '。。。(我懒了)']
	print("在这一章，我学到了:")
	for msg in messages:
		print('\t' + msg)


display_message()  # 调用函数
