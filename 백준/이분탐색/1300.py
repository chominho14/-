N=int(input())
k=int(input())

left, right = 1,k

while left<=right:    
    temp = 0
    mid = (left + right) // 2

    
    for i in range(1, N+1):
            temp += min(mid//i, N)
    
    if temp >= k:
        result = mid 
        right = mid - 1
    else:
        left = mid + 1
print(result)