# 6-11 城市

# 键
country = 'country'
population = 'population'
fact = 'fact'

cities = {  # 存储城市信息的字典
	'泸州': {
		country: '中国',
		population: 4320000,
		fact: '中国酒城'
	},
	'东京': {
		country: '日本',
		population: 13500000,
		fact: '日本首都'
	},
	'纽约': {
		country: '美国',
		population: 8620000,
		fact: '别称哥谭市'
	}
}

for city, values in cities.items():
	print("= " * 20)
	print("城市名称: " + city)
	print("所属国家: " + values[country].title())
	print("人口约数: " + str(values[population]))
	print("关于城市: " + values[fact])
