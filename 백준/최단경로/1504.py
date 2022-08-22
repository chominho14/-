import heapq

INF = int(1e9)

N, E = map(int, input().split())


graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
v1, v2 = map(int, input().split())

def dijkstra(start):
    distance = [INF] * (N + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    
    return distance
                
one = dijkstra(1)
v1_di = dijkstra(v1)
v2_di = dijkstra(v2)

v1_path = one[v1] + v1_di[v2] + v2_di[N]
v2_path = one[v2] + v2_di[v1] + v1_di[N]

result = min(v1_path, v2_path)

if result < INF:
    print(result)
else:
    print(-1)
