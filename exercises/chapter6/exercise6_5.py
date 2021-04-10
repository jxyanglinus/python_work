# 6-5 河流

# 河流信息字典
rivers = {
	"印度河": "印度",
	"长江": "中国",
	"湄公河": "缅甸"
}

# 循环打印”...河经过了...(国家)“
for river, countries in rivers.items():
	print(river + " 经过了 " + countries)
