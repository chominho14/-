
n, m = map(int, input().split())

num = []
for i in range(1, n+1):
    num.append(i)
    

for _ in range(m):
    temp_i = 0
    temp_j = 0
    
    i, j = map(int, input().split())
    temp_i = num[i-1]
    temp_j = num[j-1]
    
    num[i-1] = temp_j
    num[j-1] = temp_i

for i in num:
    print(i, end=" ")
    
    