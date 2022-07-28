from collections import deque

N = int(input())
dq = deque()

for i in range(N,0, -1):
    dq.append(i)

while len(dq) >= 2:
    dq.pop()
    dq.appendleft(dq.pop())    
    
print(dq[0])