s=input().split('-')

plus=[]

for i in s:
    cnt=0
    a=i.split('+')
    for j in a:
        cnt+=int(j)
    plus.append(cnt)
    
result=plus[0]
for k in range(1,len(plus)):
    result-=plus[k]
print(result)