N = int(input())

# 최대 입력 갯수
dp = [0]*1000001

# i-2의 인덱스 에러를 생각
dp[1] = 1
dp[2] = 2

for i in range(3,N+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
    
print(dp[N])