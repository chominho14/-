n, k = map(int, input().split())

w = [0]
v = [0]

for _ in range(n):
    w_in, v_in = map(int, input().split())
    w.append(w_in)
    v.append(v_in)


# 일차원 dp로 값을 갱신하기 보단 아에 모든 과정을 다 저장하기 위해 이차원 배열을 사용하여 풀어야한다.
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if j < w[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])
            
print(dp[n][k])