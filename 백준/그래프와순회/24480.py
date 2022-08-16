
# 코드 완성은 햇는데 메모리 초과 뭥..
# -> python3으로 제출해야 한다.


n, m, r = map(int, input().split())

# 이차원 리스트로 그래프 초기화
graph = [[]*n for _ in range(n+1)]
# 그래프 입력 받기
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = [False] * (n+1)
graph_cnt = [0] * (n+1)
cnt = 1
# DFS 함수
def dfs(graph, start, visited):
    global cnt
    # 방문시 True 값으로
    visited[start] = True
    graph_cnt[start] = cnt
    graph[start].sort(reverse=True)
    # 인접 노드 방문 검사
    for i in graph[start]:
        if not visited[i]: # 방문하지 않은 곳이면
            cnt+=1
            dfs(graph, i, visited)
            

            
            
dfs(graph, r, visited)

for i in range(1,len(graph_cnt)):
    print(graph_cnt[i])

