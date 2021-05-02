# 8-6 城市名

def city_country(city, country):
	"""返回城市和其所属国家的字符串信息"""
	result = city.title() + ', ' + country.title()
	return result


city1 = city_country('luzhou', 'china')
city2 = city_country('santiago', 'chile')
city3 = city_country('new york', 'america')

infos = [city1, city2, city3]
for info in infos:
	print(info)
