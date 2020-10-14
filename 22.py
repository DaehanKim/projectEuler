with open("p022_names.txt", 'rt', encoding='utf8') as f:
    my_file = f.read()

name_lst = [item.strip(r'"') for item in my_file.split(',')]
name_lst = sorted(name_lst)

# print(name_lst[:10])
alp_score_dict = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(1,len("ABCDEFGHIJKLMNOPQRSTUVWXYZ")+1)))
# print(alp_score_dict)
tot_score = 0 
for idx, item in enumerate(name_lst):
    tot_score += (idx+1)*sum(map(lambda x:alp_score_dict[x], item))

print(tot_score)