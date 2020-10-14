import math

def is_palindrome(num):
	return str(num) == "".join(list(str(num))[::-1])

# print(is_palindrome(1001001))
# print(is_palindrome(1001002))
lst = []
def do():
	for i in range(1000, 100, -1):
		for j in range(1000, 100, -1):
			if is_palindrome(i*j) : 
				lst.append(i*j)
				# return
do()
print(max(lst))