import math
from tqdm import tqdm
from collections import Counter

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

def mult(factor_dict, other):
	return {k : v*other for k,v in factor_dict.items()}
def to_string(factor_dict):
	factor_list = sorted(list(factor_dict.items()), key=lambda x:x[0])
	return "*".join([f"{k}^{v}" for k,v in factor_list])

num_list = []
# cnt = 0
for a in range(2,101):
	for b in range(2,101):
		fact_list = prime_fact(a)
		fact_dict = Counter(fact_list)
		a_powers_b = mult(fact_dict, b)
		num_list.append(to_string(a_powers_b))
		# cnt += 1
		# if cnt > 100 : 
			# print(num_list)
			# exit()

print(len(set(num_list)))