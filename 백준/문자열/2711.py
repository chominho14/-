
t = int(input())


for _ in range(t):
    i, w = map(str, input().split())

    index = int(i)
    front = w[0:index-1]
    back = w[index:len(w)]
    print(front, end="")
    print(back)
    