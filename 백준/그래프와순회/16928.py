from collections import deque

n, m = map(int, input().split())

graph = [i for i in range(101)]

for _ in range(n+m):
    a, b = map(int, input().split())
    graph[a] = b 
    
visited = [0] * 101
    
def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    dice = [1,2,3,4,5,6]
    
    while q:
        x = q.popleft()
        
        for i in range(6):
            nx = x + dice[i]
            
            if nx > 100:
                continue
            cnt = graph[nx]
            
            if visited[cnt] == 0:
                q.append(cnt)
                visited[cnt] = visited[x] + 1
                
                if cnt == 100:
                    return
                
bfs(1)
print(visited[100]-1)