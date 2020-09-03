import math
from tqdm import tqdm

from lib.tests import test_f
from lib.primes import get_primes
from lib.misc import *





# give the number of denested roots up to n
def f(n):
	
	denested_nums = []

	# get non squares
	#non_squares = get_non_squares(n)
	
	# get primes up to n
	#primes = get_primes(n)

	nested, unested = generate_number_combinations(n)

	table = [False] * int(1e8)

	
	# check each x for denested roots
	for x in tqdm(range(1, n+1), "Finding De-Nested Roots"):
		
		# can't check every non-square!
		# how to bound the search?

		# each root(z) + root(y) < x
		# sum of unested root terms squared = x
		# get the highest possible number for z and y
	
		"""
		if int(math.sqrt(x-1)) != math.sqrt(x-1):
			denested_nums.append(1 + math.sqrt(x-1))
		"""
		nums = []
		
	
		# case where there are two denested roots
		for i in range(1, x//2 + 1):
			
			num1 = math.sqrt(i) + math.sqrt(x-i)
			num2 = math.sqrt(i*(x-i))

			
			if int(num2) != num2:
				
				if True:
					nums.append((i, x-i, i*(x-i)))

				try: table[i**2 + (x-i)**2] = True
				except: pass

		"""
		# case where there are three denested roots
		for i in range(x):
			for j in range(x-i):

				k = x - i - j

				num1 = math.sqrt(i)
				num2 = math.sqrt(j)
				num3 = math.sqrt(k)

				num = (num1 + num2 + num3)

				if  num != int(num):

					if True:
						nums.append((i, x-i, i*(x-i)))

					try: table[i**2 + (x-i)**2] = True
					except: pass
		"""
		
		"""
		if x < 10 :	
			print(x , " | ", nums)
		
		else:
			print(x , "| ", nums)
		"""
		# include all prime numbers less than N
		# include all multiples of every number less than N
		# include all non squares less than n

		#n + (n-1) + (n-2) - n

	

	
	counter = 0
	
	for i in tqdm(range(int(1e7)),"Counting Unested Values"):
		if table[i]:
			counter+= 1
	
	return counter



def brute_trio(n):

	for x in tqdm(range(n)):

		for y in range(x**2):

			for z in range(x-y):

				for a in range(1, x):

					for b in range(1, x-a):

						for c in range(1, x-a-b):

							 

							root_z = math.sqrt(z)
							root_y = math.sqrt(y)

							if int(root_z) != root_z and int(root_y) != root_y:

								root = root_z + root_y
								roots = math.sqrt(a) + math.sqrt(b) + math.sqrt(c) - math.sqrt(x-a-b-c)

								if abs(math.sqrt(x + root) - roots) < 0.0001:
									print(x, y, z, "|", a, b, c, x-a-b-c)
									





if __name__ == "__main__":
	
	#print(test_f(f))
	
	print(brute_trio(29))
	

