from collections import deque

T = int(input())


def bfs(graph, x, y):
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    
    graph[x][y] = 0
    q = deque()
    q.append((x, y))
    
    cnt = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=M or ny<0 or ny>=N:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    return cnt 

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0]*N for _ in range(M)]
    count = []

    for _ in range(K):
        a,b = list(map(int, input().split()))
        graph[a][b] = 1
    
    
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                count.append(bfs(graph, i, j))
                
    print(len(count))
    
               
    
        
