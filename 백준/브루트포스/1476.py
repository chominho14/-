e, s, m = map(int, input().split())

a, b, c = 1, 1, 1

for i in range(1, 7981):
    if a > 15:
        a = 1
    if b > 28:
        b = 1
    if c > 19:
        c = 1
    if a==e and s==b and c==m:
        print(i)
        break
    a += 1
    b += 1
    c += 1
    