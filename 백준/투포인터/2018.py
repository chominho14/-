n = int(input())

left = 0
right = 0

cnt = 0
temp = 0

while right <= n:
    
    if temp == n:
        cnt += 1
        right += 1
        temp += right
    elif temp < n:
        right += 1
        temp += right
    else:
        temp -= left
        left += 1
    

print(cnt)


# 배열로 받아 풀면 메모리 초과


# num = []

# for i in range(1,n+1):
#     num.append(i)


# left = 0
# right = 0

# cnt = 0
# temp = 0

# while left <= right and right < n:
    
#     if temp == n:
#         cnt+=1
#         temp += num[right]
#         right += 1
#     elif temp < n:
#         temp += num[right]
#         right += 1
#     else:
#         temp -= num[left]
#         left += 1
    

# print(cnt+1)