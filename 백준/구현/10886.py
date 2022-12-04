n=int(input())
cnt=0
for _ in range(n):
    k=int(input())
    if k==1:
        cnt+=1

if n//2 >= cnt:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")