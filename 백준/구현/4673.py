dr = []

k = 1

while k < 10000:
    str_k = str(k)
    arr_k = list(str_k)
    sum_k = sum(map(int, arr_k))
    temp = k + sum_k
    k += 1    
    dr.append(temp)

for i in range(1, 10000):
    if i not in dr:
        print(i)
    