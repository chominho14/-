p = 1000 - int(input())
cnt = 0
change = [500,100,50,10,5,1]
i=0
while p!=0:
    if p>=change[i]:
        cnt+=1
        p -= change[i]
    else:
        i += 1

print(cnt)