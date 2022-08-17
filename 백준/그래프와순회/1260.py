# 코드상 문제는 없지만 틀렸습니다로 뜬다..!

# dfs, bfs 수행하기
from collections import deque

n, m, v = map(int, input().split())

graph = [[]*n for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
bfs_graph = graph
dfs_graph = graph

for i in range(n+1):
    dfs_graph[i].sort()
    
for i in range(n+1):
    bfs_graph[i].sort()
    
dfs_cnt = [0]*(n+1)
bfs_cnt = [0]*(n+1)

dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)

d_cnt = 1
b_cnt = 1

def dfs(graph, v, visited):
    global d_cnt
    visited[v] = True
    dfs_cnt[v] = d_cnt
    for i in graph[v]:
        if not visited[i]:
            d_cnt += 1
            dfs(graph, i, visited)

dfs(dfs_graph, v, dfs_visited)

def bfs(graph, v, visited):
    global b_cnt
    queue = deque([v])
    visited[v] = True
    
    while queue:
        r = queue.popleft()
        bfs_cnt[r] = b_cnt
        b_cnt += 1
        for i in graph[r]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(bfs_graph, v, bfs_visited)

for i in range(1, len(dfs_cnt)):
    print(dfs_cnt[i], end=" ")
print()
for i in range(1, len(dfs_cnt)):
    print(bfs_cnt[i], end=" ")
