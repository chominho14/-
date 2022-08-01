N = int(input())

T = []
for _ in range(N):
    start, end = map(int, input().split())
    T.append([start, end])
   
# T[0]번째를 기준으로 오름차순 
T = sorted(T, key=lambda a:a[0])
# T[1]번째를 기준으로 오름차순
T = sorted(T, key=lambda a:a[1])

last = 0
cnt = 0
for i, j in T:
    if i >= last:
        cnt += 1
        last = j

print(cnt)