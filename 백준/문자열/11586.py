n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

k = int(input())

if k==1:
    for i in range(n):
        print(arr[i])
elif k==2:
    for i in arr:
        print(i[::-1])
else:
    for i in range(n,0,-1):
        print(arr[i-1])