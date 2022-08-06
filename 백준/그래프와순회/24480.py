
# dfs
def dfs(v):
    global cnt
    visited[v] = True
    
    nodes_cnt[v] = cnt
    nodes[v].sort(reverse=True)
    
    for i in nodes[v]:
        if not visited[i]:
            cnt += 1
            dfs(i)


# 정점 수, 간선 수, 시작 정점 입력
N, M, R = map(int, input().split())

# 노드마다 연결된 곳 저장
nodes = [[] for _ in range(N+1)]
# 방문한지 안한지 저장할 배열
visited = [False]*(N+1)
# 정점 i의 방문 순서 저장 배열
nodes_cnt = [0]*(N+1)

cnt = 1

# 간선 수만큼 반복문을 돌려 간선의 꼬리와 머리를 저장
for _ in range(M):
    tail, head = map(int, input().split())
    nodes[tail].append(head)
    nodes[head].append(tail)
    
# 시작 정점에서 시작
dfs(R)

for val in nodes_cnt[1:]:
    print(val)
