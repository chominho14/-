# 떡볶이 떡 만들기

N, M = map(int, input().split())
prov_arr = list(map(int, input().split()))

start = 0
end = max(prov_arr)
result = 0

while start <= end:
    mid = (start + end) // 2
    temp = 0
    for i in range(N):
        if mid >= prov_arr[i]:
            temp += mid - prov_arr[i]
    
    if M >= temp:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)