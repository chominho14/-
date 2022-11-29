x=int(input())
n=int(input())
k=0
for _ in range(n):
    a, b = map(int, input().split())
    k+=a*b

if x==k:
    print("Yes")
else:
    print("No")