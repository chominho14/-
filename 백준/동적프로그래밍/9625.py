k = int(input())

dp_a = [0] * (k+2)
dp_b = [1] * (k+2)

dp_a[1] = 1
dp_b[1] = 1

if k>=1:
    dp_a[2] = 1
    dp_b[2] = 2

if k>2:
    for i in range(3, k+1):
        dp_a[i] = dp_a[i-1] + dp_a[i-2]
        dp_b[i] = dp_b[i-1] + dp_b[i-2]

print(dp_a[k-1], dp_b[k-1])