import math

def str_inversion(inp, limit = 20):
    start_pos = math.ceil(math.log10(inp))
    ret = [0 for _ in range(start_pos-1)]
    numerator = 10 ** start_pos
    for _ in range(limit):
        ret.append(numerator//inp)
        if numerator%inp == 0 : break 
        numerator = (numerator%inp) * 10
    return "".join(map(lambda x:str(x), ret))



# for i in range(10,20):
#     print(str_inversion(i))