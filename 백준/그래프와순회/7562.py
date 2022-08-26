from collections import deque


def bfs(bx, by, cx, cy):
    q = deque()
    q.append([bx,by])
    
    visited[bx][by] = 1
    
    dx = [1,1,2,2,-1,-1,-2,-2]
    dy = [2,-2,1,-1,2,-2,1,-1]
    
    
    while q:
        x, y = q.popleft()
        
        if x == cx and y == cy:
            print(visited[cx][cy] - 1)
            return
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=l or ny<0 or ny>=l:
                continue
            if visited[nx][ny] == 0:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y]+1
            
            
    
           
T = int(input())
      
for _ in range(T):
    l = int(input())
    night = list(map(int, input().split()))
    check = list(map(int, input().split()))
    
    visited = [[0]*(l) for _ in range(l)]
    
    bfs(night[0], night[1], check[0], check[1])
