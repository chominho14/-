# 연산의 갯수에만 집중하자
n = int(input())

dp = [0]*(n+1)
# 1이 1이 되는 경우는 연산이 0이므로 2부터 시작
for i in range(2, n+1):
    # 3.
    dp[i] = dp[i-1] + 1
    # 1.
    if i%3 == 0:
       dp[i] = min(dp[i//3]+1, dp[i])
    # 2.
    if i%2 == 0:
        dp[i] = min(dp[i//2] + 1, dp[i])

print(dp[n])