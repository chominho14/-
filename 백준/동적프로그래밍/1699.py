n = int(input())

dp=[100001] * (n+1)

dp[0] = 0
# 100000의 제곱근 최대 범위로 잡아서 돌리면 메모리는 조금 들지만 시간이 30배 넘게 차이난다.
for i in range(1, round(n**(1/2))+1):
    num = i*i
    for j in range(num, n+1):
        dp[j] = min(dp[j], dp[j-num] + 1)

print(dp[n])