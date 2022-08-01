N, K = map(int, input().split())
prov = list(map(int, input().split()))

# 배열에 누적 합을 구해 놓는다.
idx = []
temp = 0
for i in prov:
    temp += i
    idx.append(temp)

# 누적합을 이용하여 K개만큼의 합들을 배열에 저장한뒤 최댓값을 출력
result = []
for i in range(N-K+1):
    if i == 0:
        result.append(idx[K-1])
    else:
        result.append(idx[K+i-1] - idx[i-1])
 
print(max(result))