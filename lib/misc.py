import math
from tqdm import tqdm

def get_unested_root(l):
	num = 0
	for i in l:
		num+=math.sqrt(i)
	return num

# get all non perfect squares
def get_non_squares(n):
	non_squares = []
	for i in tqdm(range(n+1), "Getting Non-Squares"):
		num = math.sqrt(i)
		if num != int(num):
			non_squares.append(i)

	return non_squares


# gets the unested values using the wiki formula (https://en.wikipedia.org/wiki/Nested_radical)
def get_unested(x, y, z):

	s1 = (x + math.sqrt(x**2 - (math.sqrt(y)+math.sqrt(z))) )/2
	s2 = (x - math.sqrt(x**2 - (math.sqrt(y)+math.sqrt(z))) )/2

	s1 = math.sqrt(s1)
	s2 = math.sqrt(s2)

	return s1-s2, s1+s2

# generate possible unested root terms
def generate_number_combinations(n):
	
	nested = generate_nested_roots(n)
	unested = generate_unested_roots(n)

	return nested, unested

# generate possible y and z terms
def generate_nested_roots(n):
	
	# have to be divisble by 4
	# sqrt(y) + sqrt(z) < x

	nested_nums = []
	for i in range(1, n):

		if i < n//9 and int(math.sqrt(i))!= math.sqrt(i):
			nested_nums.append(i)

		elif (i%4 == 0 or i%9 == 0) and int(math.sqrt(i))!= math.sqrt(i):
			nested_nums.append(i)			
	
	return nested_nums			

# generate unested term
def generate_unested_roots(n):

	# have to add up to n
	pass

def generate_hash_table(n):

	root_table = {}

	for i in tqdm(range(n), "Generating Root Table"):
		num = math.sqrt(i)
		if num != int(num):
			root_table[round(num, 5)] = i


def cheat_two_root(n):

	non_squares = get_non_squares(n)

	sum_num = (n**2 - n) - (n**2 - n)/2 -n

	square_terms = 0
	
	sqr_counter = 0
	
	for i in tqdm(range(1, n), "Adding Perf Squares"):
		
		if i**2 >= n:
			break
			
		square_terms += n - i**2
		sqr_counter += 1

	return sum_num - square_terms - sqr_counter