# dp 문제
# 역순으로 생각해야 한다!

n = int(input())

t = []
p = []
dp = [0 for _ in range(n+1)]

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    
for i in range(n-1, -1, -1):
    
    # 퇴사일 보다 값이 클 경우
    if t[i] + i > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], p[i] + dp[t[i] + i])
    
print(dp[0])
    
        
    