n = int(input())

dp = [0]*(n+1)
# SK = 1, CY = 2
dp[1] = 1
if n>1:
    dp[2] = 2
if n>2:
    dp[3] = 1
if n>3:
    for i in range(4,n+1):
        if dp[i-1] == 1 or dp[i-3] == 1:
            dp[i] = 2
        else:
            dp[i] = 1


if dp[n] == 1:
    print("SK")
else:
    print("CY")