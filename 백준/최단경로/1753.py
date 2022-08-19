
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

import heapq

v1, e = map(int, input().split())
k = int(input())

INF = int(1e9)

graph = [[] * (v1+1) for _ in range(v1+1)]
distance = [INF] * (v1 + 1)

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))
    


def dijkstra(start):
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
                
dijkstra(k)

for i in range(1, v1+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
