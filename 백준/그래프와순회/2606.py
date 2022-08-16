
n = int(input())
m = int(input())

# 이차원 리스트로 그래프 초기화
graph = [[]*n for _ in range(n+1)]
# 그래프 입력 받기
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = [False] * (n+1)
cnt = 0
# DFS 함수
def dfs(graph, start, visited):
    global cnt
    # 방문시 True 값으로
    visited[start] = True
    # 인접 노드 방문 검사
    for i in graph[start]:
        if not visited[i]: # 방문하지 않은 곳이면
            dfs(graph, i, visited)
            cnt+=1
            
dfs(graph, 1, visited)

print(cnt)