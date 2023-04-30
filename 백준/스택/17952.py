n = int(input())
score = 0
s = [0]
sc = [0]

for _ in range(n):
    i = list(input().split())
    
    
    if i[0] == '1':
        sc.append(i[1])
        s.append(i[2])
        l = int(s[-1])
        l -= 1
        
        if l == 0:
            s.pop()
            score += int(sc.pop())
        else:
            s[-1] = str(l)
    else:
        l = int(s[-1])
        l -= 1
        s[-1] = str(l)
        
        if l == 0:
            s.pop()
            score += int(sc.pop())
        else:
            s[-1] = str(l)

print(score)
            