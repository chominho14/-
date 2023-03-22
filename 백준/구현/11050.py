n, k = map(int, input().split())

t=1
for i in range(2, n+1):
    t *= i

b=1
for i in range(2, k+1):
    b *= i

b_s=1
for i in range(2, n-k+1):
    b_s *= i
    
print(int(t/(b*b_s)))