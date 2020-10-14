import math
from itertools import combinations


lst = range(1,101)
sum = 0
for i,j in combinations(lst, 2):
	sum += i*j

print(2*sum)