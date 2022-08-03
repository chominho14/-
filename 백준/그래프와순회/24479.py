# 공부 더 하기!!!

# 깊이 우선 탐색(dfs)
N, M, R = map(int, input().split())
# 연결노드 그래프 초기화 [[],[],[],[],[],...,[]]
graph = [[] for _ in range(N+1)]
# 방문 순서 그래프
visted = [0]*(N+1)
cnt = 1

# 깊이 우선 탐색 (연결노드 그래프, 정점, 방문 순서 그래프)
def dfs(graph, v, visted):
    global cnt
    # 방문한 정점에 cnt 값을 넣어 준다.
    visted[v] = cnt
    
    for i in graph[v]:
        # 만약 방문 안한 정점이라면 방문
        if visted[i] == 0:
            cnt += 1
            # 연결된 노드 안에 또 탐색
            dfs(graph, i, visted)

# u, v를 입력받아 그래프에 방문해야 될 정점들 저장
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
# 정점 오름차순
for i in range(N + 1):
    graph[i].sort()
    
# 탐색 시작
dfs(graph, R, visted)

# N+1까지 1번째부터 출력
for i in range(N+1):
    if i != 0:
        print(visted[i])