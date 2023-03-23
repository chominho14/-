# import math

n, k = map(int, input().split())

# 이항계수 구조로 dp를 만들어 둔다.
dp = [1]
for i in range(2, n+2):
    dp.append(i*[1])
    
for i in range(2, n+1):
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print(dp[n][k] % 10007)


# 출력 초과

# dp_t=[1]*(n+1)
# for i in range(2, n+1):
#     dp_t[i] = dp_t[i-1] + 1

# dp_b=[1]*(k+1)
# dp_bs=[1]*(n-k+1)


# for i in range(2, k+1):
#     dp_b[i] = dp_b[i-1] + 1

# for i in range(2, n-k+1):
#     dp_bs[i] = dp_bs[i-1] + 1
    
# dp=[1] * (n+1)
# for i in range(2, n+1):
#     for j in range(1, k+1):
#         dp[i] = dp[i]
    
# print(dp_t, dp_b, dp_bs)
# print(int(math.prod(dp_t)/(math.prod(dp_b)*math.prod(dp_bs))))