from collections import deque


def bfs(x, y):
    dx = [1,-1,0,0,-1,-1,1,1]
    dy = [0,0,1,-1,1,-1,1,-1]
    
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    while q:
        a, b = q.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if 0<=nx<h and 0<=ny<w:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    q.append((nx, ny))
                    
while True:
    w, h = map(int, input().split())
    if w==0 and h==0:
        break
    graph = []
    
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    
    cnt=0
    
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i,j)
                cnt += 1
    
    print(cnt)
                
    
