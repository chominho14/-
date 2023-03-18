n=int(input())
cards = list(map(int, input().split()))

dp = [0]*(n+1)

dp[1] = cards[0]

# 카드의 번호가 1부터 n까지 이므로 반복
for i in range(1, n+1):    
    # DP 시작
    for j in range(i, n+1):
        dp[j] = max(dp[j], dp[j-i]+cards[i-1])
        
print(dp[n])