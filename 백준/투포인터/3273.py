# 특정한 합을 가지는 부분 연속 수열 찾기
n = int(input()) # 데이터의 개수 n
data = list(map(int, input().split())) # 전체 수열
x = int(input()) 

count = 0
start = 0
end = n-1
data.sort()

while start < end:
    temp = data[start] + data[end]
    
    if temp == x:
        count += 1
        start += 1
    elif temp < x:
        start += 1
    else:
        end -= 1
    
print(count)