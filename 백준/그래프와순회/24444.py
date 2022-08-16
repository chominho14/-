# 너비 우선 탐색
from collections import deque
import sys

# n, m, r = map(int, input().split())
n, m, r = map(int,sys.stdin.readline().split())

graph = [[]*n for _ in range(n+1)]

for _ in range(m):
    # a, b = map(int, input().split())
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False] * (n+1)
graph_cnt = [0] * (n+1)
cnt = 1

# 오른 차순 정렬
for i in range(n+1):
    graph[i].sort()


def bfs(r):
    global cnt
    # 시작 정점부터 큐 생성
    queue = deque([r])
    visited[r] = True

    while queue:
        v = queue.popleft()
        graph_cnt[v] = cnt # 큐에 있는 노드에 순서에 따라 카운트 넣기
        cnt += 1
        for i in graph[v]:
            if not visited[i]: # 방문한 곳이 아니라면
                queue.append(i) # 큐에 노드 담기
                visited[i] = True # 방문한 곳은 True로 값 바꾸기

bfs(r)

for i in range(1,len(graph_cnt)):
    print(graph_cnt[i])