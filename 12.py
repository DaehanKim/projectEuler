import math
from tqdm import tqdm
from functools import reduce
from collections import Counter

lim = 1000000


def is_prime(num):
	if num == 2: return True
	for i in range(2, math.ceil(math.sqrt(num))+1):
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


def get_num_divisor(num):
	cnt = Counter(prime_fact(num))
	ret = 1
	for v in cnt.values():
		ret*=(v+1)
	return ret





for i in tqdm(range(1,lim)):
	num_div = get_num_divisor(i*(i+1)//2)
	if num_div > 500:
		print("")
		print(i*(i+1)//2)
		break
