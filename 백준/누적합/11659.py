N, M = map(int, input().split())
prov = list(map(int,input().split()))

# 0~n 까지 더한 값들을 미리 배열에 저장한다
idx = [0]

temp = 0
for i in prov:
    temp += i
    idx.append(temp)
    
print(idx)
for _ in range(M):
    i, j = map(int, input().split())
    print(idx[j] - idx[i-1])


# 시간 복잡도 O(n^2)

# for _ in range(M):
#     i, j = map(int, input().split())
#     result = 0
#     for k in range(i-1, j):
#         result += prov[k]
#     print(result)