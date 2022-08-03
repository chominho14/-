
# dp 메모이제이션(하향식)
def wFn (a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
         return 1;
    if a > 20 or b > 20 or c > 20:
        return wFn(20, 20, 20)
    
    # 재귀와 다른 점. (같은 값이 있다면 바로 찾아 리턴)
    if dp[a][b][c]:
        return dp[a][b][c]
    
    if a < b and b < c:
        dp[a][b][c] = wFn(a, b, c-1) + wFn(a, b-1, c-1) - wFn(a, b-1, c)
        return dp[a][b][c]
    
    dp[a][b][c] = wFn(a-1, b, c) + wFn(a-1, b-1, c) + wFn(a-1, b, c-1) - wFn(a-1, b-1, c-1)
    return dp[a][b][c]
        
dp = [[[0]*21 for _ in range(21)] for _ in range(21)]

while True:
    a, b, c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break
    print(f"w({a}, {b}, {c}) = {wFn(a,b,c)}")
    
        