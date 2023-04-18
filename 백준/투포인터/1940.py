n = int(input())
m = int(input())

ingre = list(map(int, input().split()))

left = 0
right = n-1

cnt = 0

ingre.sort()

while right < n and left < right:
    com_num = ingre[left] + ingre[right]
    if  com_num == m:
        cnt += 1
        right -= 1
    elif com_num < m:
        left += 1
    else:
        right -= 1
        
print(cnt)