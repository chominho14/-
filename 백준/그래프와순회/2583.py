from collections import deque

m, n, k = map(int, input().split())

graph = [[1] * n for _ in range(m)]

for i in range(k):
    lx, ly, rx, ry = map(int, input().split())
    for j in range(lx,rx):
        for k in range(ly,ry):
            graph[k][j] = 0
                
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(x, y):
    q = deque()
    q.append((x,y))
    graph[x][y] = 0
    cnt = 1
    while q:
        bx, by = q.popleft()
        for i in range(4):
            nx = bx + dx[i]
            ny = by + dy[i]
            
            if 0<=nx<m and 0<=ny<n:
                if graph[nx][ny]==1:
                    graph[nx][ny] = 0
                    cnt += 1
                    q.append((nx, ny))
    return cnt

result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            graph[i][j] = 0
            result.append(bfs(i, j))
print(len(result))
result.sort()
for i in result:
    print(i, end=" ")