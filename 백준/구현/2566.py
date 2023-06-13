
num=[]

for _ in range(9):
    num.append(input().split())
    
l = 0
r = 0
temp = 0

for i in range(9):
    for j in range(9):
        if temp <= int(num[i][j]):
            l = i+1
            r = j+1
            temp = int(num[i][j])
    
print(temp)
print(l, r)