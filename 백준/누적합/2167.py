n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr_s = [[0]*(m+1) for _ in range(n)]

# 누적합 이용
for i in range(n):
    cnt = 0
    for j in range(m):
        cnt += arr[i][j]
        arr_s[i][j+1] = cnt

k = int(input())


for _ in range(k):
    i, j, x, y = map(int, input().split())
    result = 0
    for k in range(i-1, x):
        result += arr_s[k][y] - arr_s[k][j-1]

    print(result)





# 시간 초과
# for _ in range(k):
#     i, j, x, y = map(int, input().split())
#     result = 0
#     for k in range(i-1, x):
#         for l in range(j-1, y):
#             result += arr[k][l]

#     print(result)