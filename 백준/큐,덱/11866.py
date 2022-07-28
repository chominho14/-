from collections import deque

N, K = map(int, input().split())
dq = deque()
result = []

for i in range(1,N+1):
    dq.append(i)

while dq:
    for i in range(K-1):
        dq.append(dq.popleft())
    result.append(dq.popleft())
        
    
print("<", end="")
for i in range(len(result) - 1):
    print("%d, "%result[i], end="")
print(result[-1],end="")
print(">")
