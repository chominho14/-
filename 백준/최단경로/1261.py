from collections import deque

m, n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

distance = [[-1] * m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

q = deque()
q.append((0,0))
distance[0][0] = 0
while q:
    x, y = q.popleft()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<n and 0<=ny<m:
            if distance[nx][ny] == -1:
                if graph[nx][ny] == 0:
                    distance[nx][ny] = distance[x][y]
                    q.appendleft((nx, ny))
                else:
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))
                    
print(distance[n-1][m-1])