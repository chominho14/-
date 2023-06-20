
s = list(map(int, input().split()))

s.sort()

cnt=0
if s[0] == s[1]:
    cnt += 1
if s[1] == s[2]:
    cnt += 1
    

result = 0

if cnt == 0:
    result = s[2]*100
if cnt == 1:
    result = 1000 + s[1]*100
if cnt == 2:
    result = 10000 + s[1]*1000

print(result)
