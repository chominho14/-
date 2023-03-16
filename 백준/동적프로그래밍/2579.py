n = int(input())

st = []
for i in range(n):
    st.append(int(input()))
    
dp = [0] * (n+1)

dp[1] = st[0]
if n>1:
    dp[2] = st[0] + st[1]

if n > 2:
    for i in range(3, n+1):
        # 2번째 전 계단 까지와 현재 계단을 합친 거, 3번째 계단 전과 1계단 전 현재 계단 합친 거와 비교
        dp[i] += max(dp[i-2] + st[i-1], dp[i-3] + st[i-2] + st[i-1])

print(dp[n])