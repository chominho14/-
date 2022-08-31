from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start):    
    q = deque()
    q.append(start)
    visited[start] = True
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

cnt = 0
for i in range(1,n+1):
    if not visited[i]:
        cnt+=1
        bfs(i)

print(cnt)
        
        