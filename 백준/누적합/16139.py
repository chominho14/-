import string
import sys
S = input()
q = int(input())

# 방법 2 

c_list = {}

for c in string.ascii_lowercase:
    c_list[c] = [0]
    cnt = 0
    for i in range(len(S)):
        if S[i] == c:
            cnt+= 1
        c_list[c].append(cnt)

for _ in range(q):
    a, l, r = sys.stdin.readline().rstrip().split()
    lInt = int(l)
    rInt = int(r)
    print(c_list[a][rInt+1] - c_list[a][lInt])
    
    

# 방법 1 - 50점
# for i in range(q):
#     a, l, r = input().split()
#     lInt = int(l)
#     rInt = int(r)
    
#     cnt = 0
#     for j in range(lInt, rInt + 1):
#         if S[j] == a:
#             cnt += 1
#     print(cnt)