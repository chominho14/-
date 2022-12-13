import sys
input = sys.stdin.readline

n = int(input())
l = []

for _ in range(n):
	l.append(int(input()))
cnt = 0
max = 0
for x in reversed(l):
	if max < x:
		max = x
		cnt += 1
print(cnt)