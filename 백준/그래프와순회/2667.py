from collections import deque


N = int(input())

graph = []


for _ in range(N):
    graph.append(list(map(int, input())))


def bfs(graph, x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 1
    graph[x][y] = 0    
    q = deque()
    q.append((x, y))
    
    while q:    
        x, y =  q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or nx>=N or ny<0 or ny>=N:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                 graph[nx][ny] = 0
                 q.append((nx, ny))
                 cnt += 1
    return cnt

count = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            count.append(bfs(graph, i,j))

count.sort()
print(len(count))
for i in range(len(count)):
    print(count[i])  
    
    