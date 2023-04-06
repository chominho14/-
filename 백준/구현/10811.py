n, m = map(int, input().split())

s = []

for i in range(n):
    s.append(i+1)

for _ in range(m):
    i, j = map(int, input().split())
    
    s_l = s[:i-1]
    s_c = s[i-1:j]
    s_r = s[j:]
    
    s_l.extend(reversed(s_c))
    s_l.extend(s_r)
    
    s = s_l

for i in s:
    print(i , end=" ")