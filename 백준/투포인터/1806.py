n, s = map(int, input().split())
prov = list(map(int, input().split()))

i, j = 0, 0
sum = prov[0]
ans = 100001

while True:
    if sum >= s:
        sum -= prov[i]
        ans = min(ans, j - i + 1)
        i += 1
    else:
        j += 1
        if j == n:
            break
        sum += prov[j]
    
if ans == 100001:
    print(0)
else:
    print(ans)