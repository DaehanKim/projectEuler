import math
from tqdm import tqdm



def is_abundant(num): 
    if num < 6 : return -1
    proper_divisors = [i for i in range(1, math.ceil(num/2)+1) if num % i==0]
    # print(f"{num} --> {proper_divisors}")
    return sum(proper_divisors) > num

abundant_num_list = [i for i in tqdm(range(12,28124), desc="generate abundant nums") if is_abundant(i)]

# def is_expressed(num):
#     # is_expressed_with_sum_of_two_abundant_numbers
#     for ab_num in abundant_num_list: 
#         if ab_num >= num : break
#         if num-ab_num in abundant_num_list : 
#             # print(f"{num} = {ab_num} + {num-ab_num}")
#             return True
#     return False

all_sums_below_limit = [i+j for i in tqdm(abundant_num_list, desc="get all possible sums") for j in abundant_num_list if i+j < 28124]
all_sums_below_limit = set(all_sums_below_limit)
# print(len(abundant_num_list))

sum_ = 23*24/2
for cand in tqdm(range(25, 28124), desc="get non-expressible nums"):
    if cand not in all_sums_below_limit:
        sum_ += cand

print(sum_)