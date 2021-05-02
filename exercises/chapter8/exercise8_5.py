# 8-5 城市

def describe_city(city, country='china'):
	"""某个城市属于某个国家"""
	print(city.title() + ' is in ' + country.title() + '.')


describe_city('luzhou')
describe_city('guizhou')
describe_city('tokyo', 'japan')
