t = int(input())

for i in range(t):
    arr = list((input().split()))
    for j in arr:
        k = ''.join(reversed(j))
        print(k, end=" ")
   