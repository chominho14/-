
n = int(input())

# n = 1일 경우 len(d) 가 2이므로 n+2개 까지 잡아줘야 한다.
d=[0]*(n+2)

d[1], d[2] = 1, 1

# 이친수 규칙
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])