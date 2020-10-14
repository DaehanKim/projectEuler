import math
# from functools import reduce
from collections import Counter

def is_prime(num):
	if num in (2,1): return True
	for i in range(math.ceil(math.sqrt(num)), 1, -1):
		if num % i == 0 : return False
	return True 

def get_largest_prime_factor(num):
	if is_prime(num) : return int(num)
	for i in range(math.ceil(math.sqrt(num)), 1, -1):
		if num % i == 0 and is_prime(i): return i
		


def prime_fact(num):
	factors = []
	result = num
	while(True):
		fact = get_largest_prime_factor(result)
		factors.append(fact)
		result /= fact
		if int(result) == 1 : break
	return factors



for i in range(2,21):
	print(Counter(prime_fact(i)))

ans = 19*17*2*2*2*2*3*3*5*7*11*13
print(ans)
