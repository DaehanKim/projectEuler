def str_sum(inp, other):
    def pad(inp, num_pad):
        # pad at the front part of a num
        if isinstance(inp, str): 
            return "0"*num_pad + inp
        elif isinstance(inp, list):
            return [0 for _ in range(num_pad)] + inp

    def is_flat(num_lst):
        for item in num_lst:
            if item // 10 > 0 : return False
        return True 

    def level_digits(num_lst):
        # make results flat
        temp_num_lst = num_lst[:]
        while(True):
            if temp_num_lst[0] // 10 > 0 : temp_num_lst = pad(temp_num_lst,1)
            for i in range(1,len(temp_num_lst)) : 
                temp_num_lst[-i-1] += (temp_num_lst[-i]//10)
                temp_num_lst[-i] = temp_num_lst[-i]%10
                
            if is_flat(temp_num_lst):
                break
        return temp_num_lst 

    num_pad = max(len(inp), len(other)) - min(len(inp), len(other))
    if len(inp) > len(other):
        temp_inp = inp[:]
        temp_other = pad(other, num_pad)
    else:
        temp_inp = pad(inp, num_pad)
        temp_other = other[:]
    
    res = [int(i) + int(j) for i, j in zip(temp_inp, temp_other)]
    return "".join(map(lambda x:str(x),level_digits(res)))

# a = str_sum('1323223','9434343')
# print(a)


x1, x2 = "1", "1"
idx = 2
while(len(x2) != 1000):
    temp_res = str_sum(x1, x2)
    x1, x2 = x2, temp_res
    idx += 1

print(idx)

