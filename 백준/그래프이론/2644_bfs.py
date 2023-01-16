from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

queue = deque([a])
visited[a] = 1

while queue:
    x = queue.popleft()
    if x == b:
        break
    
    for y in graph[x]:
        if visited[y] == 0:
            visited[y] = visited[x] + 1
            queue.append(y)

if visited[b] == 0:
    print(-1)
else:
    print(visited[b]-1)
        
    
    