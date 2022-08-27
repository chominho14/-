a = input().upper()

uni = list(set(a))

cnt_lst = []
for i in uni:
    cnt = a.count(i)
    cnt_lst.append(cnt)
    
if cnt_lst.count(max(cnt_lst)) > 1:
    print("?")
else:
    max_idx = cnt_lst.index(max(cnt_lst))
    print(uni[max_idx])