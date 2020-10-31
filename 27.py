import math
from tqdm import tqdm

def is_prime(num):
	if num == 2 : return True
	for i in range(math.ceil(math.sqrt(num)),1,-1):
		if num%i == 0 : return False
	return True

def get_consecutive_prime_cnt(a,b):
	n = 0
	while(True):
		target = n**2 + n*a + b
		if target <= 1 or not is_prime(target) : break
		n += 1
	return n


consecutive_prime_cnts = []
for a in tqdm(range(-999, 1000)):
	for b in range(-1000, 1001):
		consecutive_prime_cnts.append((get_consecutive_prime_cnt(a,b), a*b))

print(get_consecutive_prime_cnt(-79, 1601))
print(get_consecutive_prime_cnt(1, 41))
consecutive_prime_cnts = sorted(consecutive_prime_cnts, key=lambda x:-x[0])
print(dict(consecutive_prime_cnts))
print(f"product of coefficients : {consecutive_prime_cnts[0][1]}")