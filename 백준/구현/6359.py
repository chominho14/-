t = int(input())

for _ in range(t):
    n = int(input())
    result = 0 
    for i in range(1, n):
        if i**2 <= n:
            result += 1
        if i**2 > n:
            break
            
    print(result)