from collections import deque

import copy # deepcopy 사용

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs():
    q = deque()
    # 그래프를 deepcopy 한 후 2인 것을 모두 deque에 담는다.
    tmp_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                q.append((i, j))
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if tmp_graph[nx][ny] == 1:
                continue
            if tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                q.append((nx,ny))
    global result
    cnt = 0
    
    for i in range(n):
        # tmp_graph에 0의 갯수를 구한다.
        cnt += tmp_graph[i].count(0)
    
    result = max(result, cnt)
    
# 벽을 세워주는 함수 하나 더 필요하다.
def wall(cnt):
    # 벽이 3개 모두 세워지면 bfs시작
    if cnt == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(cnt + 1)
                graph[i][j] = 0
    
    
result = 0
# 벽을 세워 주면서 시작한다.
wall(0)
print(result)


