import math
from tqdm import tqdm

def get_primes(n):

	primes = [2]

	for i in tqdm(range(3, n), "Getting Primes"):
		
		is_prime = True

		for p in primes:
		
			if i % p == 0:
				is_prime = False
				break
			
			if p > math.sqrt(i):
				is_prime = True
				break
		
		if is_prime:
			primes.append(i)

	return primes

if __name__ == "__main__":
	primes = get_primes(int(math.sqrt(600851475143)))


