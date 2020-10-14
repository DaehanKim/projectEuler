import math
from functools import reduce
from tqdm import tqdm

def get_d(num): 
    if num < 6 : return -1
    proper_divisors = [i for i in range(1, math.ceil(num/2)+1) if num % i==0]
    # print(f"{num} --> {proper_divisors}")
    return sum(proper_divisors)        

def get_amicable_numbers():
    sum_of_proper_divisors = [get_d(num) for num in range(1,10001)]
    # print(sum_of_proper_divisors)
    return [item for idx,item in tqdm(enumerate(sum_of_proper_divisors)) if item != -1 and get_d(item) == idx+1 and get_d(item) != item]

# find all amicable numbers under 10000
sum_ = reduce(lambda x,y : x+y, get_amicable_numbers())
print(sum_)

# print(get_amicable_numbers())
# get_amicable_numbers()