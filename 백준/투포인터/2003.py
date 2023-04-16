n, m = map(int, input().split())
a = list(map(int, input().split()))

cnt = 0
left = 0
right = 1

while right <= n and left <= right:
    sum_a = sum(a[left:right])
    
    if sum_a == m:
        cnt += 1
        right += 1
    elif sum_a > m:
        left += 1
    else:
        right += 1

print(cnt)

# 시간초과
# for i in range(n):
#     left = i
#     right = i+1
#     for j in range(n-i):
#         if m == sum(a[left:right+j]):
#             cnt += 1

# print(cnt)