n, k = map(int, input().split())
temp = list(map(int, input().split()))

result = []

for i in range(n-k+1):
    s=0
    for j in range(i,i+k):
        s+=temp[j]
    result.append(s)

print(max(result))