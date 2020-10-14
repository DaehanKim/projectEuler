import math

def is_prime(n):
	for i in range(2,math.ceil(math.sqrt(n))):
		if n%i ==0 : return False
	return True

TARGET =  600851475143 

for i in range(math.ceil(math.sqrt(TARGET)),1,-1):
	# print(i)
	# break
	if TARGET % i == 0 and is_prime(i): 
		print(i)
		break  