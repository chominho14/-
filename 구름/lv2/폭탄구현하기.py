
n, k = map(int, input().split())

def plus(bx, by, graph):
	dx = [1,-1,0,0]
	dy = [0,0,1,-1]	
	graph[bx][by] += 1
	for i in range(4):
		x = bx + dx[i]
		y = by + dy[i]
		if x<=n and x>0 and y<=n and y>0:
			graph[x][y] += 1
			
	

graph = [[0]*(n+1) for i in range(n+1)]

for i in range(k):
	x, y = map(int, input().split())
	plus(x, y, graph)

result = 0
for i in range(n+1):
	for j in range(n+1):
		result += graph[i][j]
print(result)
	
	