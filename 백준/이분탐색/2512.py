N = int(input())
req = list(map(int, input().split()))
M = int(input())

start = 1
end = max(req)
result =0

while start <= end:
    mid = (start + end) // 2
    
    temp = 0
    for i in range(N):
        if mid >= req[i]:
            temp += req[i]
        else:
            temp += mid
    if temp > M:
        end = mid - 1
         
    else:
        start = mid + 1  
        
        
           
print(end)