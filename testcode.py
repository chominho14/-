T = int(input())
s = []

for _ in range(T):
    s.append(input())
    
for i in range(T):
    cnt = 0
    
    for j in range(len(s[i])):
        if cnt >= 0:
            if s[i][j] == "(":
                cnt += 1
            else:
                cnt -= 1
        else:
            continue
    if cnt == 0:
        print("YES")
    else:
        print("NO")