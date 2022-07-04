
N, M= map(int, input().split())
card_lst=list(map(int, input().split()))

card_lst.sort()

result=[]

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            sum = card_lst[i]+card_lst[j]+card_lst[k]
            if sum <= M:
                result.append(sum)
            sum=0
result.sort()
print(result[-1])