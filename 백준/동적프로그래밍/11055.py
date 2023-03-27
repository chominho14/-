# 아직 잘 이해가 안 된다. 흠...
# 다시 풀어보기

n = int(input())
a = list(map(int, input().split()))

dp = [0] * (n)
dp[0] = a[0]

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + dp[i])
        else:
            dp[i] = max(dp[i], a[i])
    
print(max(dp))
