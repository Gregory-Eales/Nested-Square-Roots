message = "algorithm failure @ f({}): got {} instead of {}"

def test_set(a, b, f):
	r = f(a)
	if r != b:
		print(message.format(a, r, b))

def test_f(f):

	print("-"*85)

	pairs = [[10, 17], [15, 46], [20, 86], [30, 213], [100, 2918], [5000, 11134074]]

	for pair in pairs:
		test_set(pair[0], pair[1], f)


	print("-"*85)