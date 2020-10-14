import math

def is_prime(num):
	if num == 2 : return True
	for i in range(math.ceil(math.sqrt(num)),1,-1):
		if num%i == 0 : return False
	return True


lim = int(1e100)
cnt = 0
for i in range(2,lim):
	if is_prime(i) : 
		cnt += 1
		# print(f"{cnt}th prime : {i}")
	if cnt == 10001 : 
		print(i)
		break