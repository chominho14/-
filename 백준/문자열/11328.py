t = int(input())

for i in range(t):
    f, s = map(str, input().split())
    f_sort = sorted(f)
    s_sort = sorted(s)
    if f_sort == s_sort:
        print("Possible")
    else:
        print("Impossible")