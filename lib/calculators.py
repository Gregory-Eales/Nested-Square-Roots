import math


# calculate nested root
def calc_nested_root(x,y,z):
	"""
	calculates the nested root value from x, y, z
	"""
	return math.sqrt(x + math.sqrt(y) + math.sqrt(z))
