from collections import deque

n = int(input())

graph = []

# 높이에 해당하는 반복문을 돌릴때 최대 높이를 먼저 구해 100번 반복할 걸 줄인다.
maxNum = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] > maxNum:
            maxNum = graph[i][j]
    

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(x, y, h, visited):
    q = deque()
    q.append((x, y))
    
    visited[x][y] = True
    while q:
        bx, by = q.popleft()
        
        for i in range(4):
            nx = bx + dx[i]
            ny = by + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] > h and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    
# 최대 높이까지 반복
result = 0
for i in range(maxNum):
    # 매번 visited를 초기화
    visited = [[False]*(n) for _ in range(n)]
    cnt = 0
    
    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == False:
                bfs(j, k, i, visited)
                cnt += 1
                
    if result < cnt:
        result = cnt

print(result)