import sys

n=int(input())
a=list(map(int, sys.stdin.readline().split()))

result = [0]
p=0

for i in range(n):
    p += a[i]
    result.append(p)

m=int(sys.stdin.readline())

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())    
    print(result[j]-result[i-1])