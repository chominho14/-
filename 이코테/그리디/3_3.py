N, M = map(int, input().split())

result = []


for i in range(N):
    r = list(map(int, input().split()))
    result.append(min(r))
    
print(max(result))