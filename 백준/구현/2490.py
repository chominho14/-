
for i in range(3):
    t_arr = list(map(int, input().split()))
    t_cnt=t_arr.count(1)
    if t_cnt==3:
        print("A")
    elif t_cnt==2:
        print("B")
    elif t_cnt==1:
        print("C")
    elif t_cnt==0:
        print("D")
    else:
        print("E")
    