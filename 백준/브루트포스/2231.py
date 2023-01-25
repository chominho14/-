n=int(input())

for i in range(1,n+1):
    con = sum(list(map(int, str(i))))
    if con+i == n:
        print(i)
        break
    if i == n:
        print(0)

    