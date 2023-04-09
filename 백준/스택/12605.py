t = int(input())

for i in range(t):
    l = list(map(str, input().split()))
    l_reverse = l[::-1]
    print("Case #",end="")
    print(i+1,end="")
    print(":",end=" ")
    for j in l_reverse:
        print(j, end=" ")