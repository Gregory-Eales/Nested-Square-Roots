


def test_f(f):
	print("-"*85)
	r = f(10)
	if r != 17:
		return "Algorithm Failure @ f({}): got {} instead of {}".format(10, r, 17)
	
	r = f(15)
	if r != 46:
		return "Algorithm Failure @ f({}): got {} instead of {}".format(15, r, 46)
	
	r = f(20)
	if r != 86:
		return "Algorithm Failure @ f({}): got {} instead of {}".format(20, r, 86)
	
	"""	
	if f(30) != 213:
		return "Algorithm Failure @ f({})".format(30)
	
	
	if f(100) != 2918:
		return "Algorithm Failure @ f({})".format(100)
	
	
	if f(5000) != 11134074:
		return "Algorithm Failure @ f({})".format(5000)

	"""

	return "Algorithm Success"