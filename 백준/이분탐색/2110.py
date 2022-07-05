# 아직 풀이 이해를 다 하지 못 함..

N, C = map(int, input().split())
house_lst=[]

for _ in range(N):
    house_lst.append(int(input()))

house_lst.sort()

start, end = 1, house_lst[N-1] - house_lst[0]
result = 0

# 만약 공유기 설치를 2대만 한다면 처음과 끝 값
if C == 2:
    print(house_lst[N-1] - house_lst[0])
else:
    # 이분 탐색
    while start < end:
        mid = (start + end) // 2
        count = 1
        wifi = house_lst[0]
        
        # 마지막으로 설치된 공유기의 위치
        for i in range(N):
            if house_lst[i] > mid + wifi:
                count += 1
                wifi = house_lst[i]
        
        if count >= C:
            result = count
            start = mid + 1
        else:
            end = mid - 1
    print(result)








# 시간 초과 풀이

# 비교할 최솟 값은 1, 최댓 값은 가장 큰 값 - 1로 지정
# left, right = 1, max(house_lst) - 1

# if C == 2:
#     print(house_lst[N-1] - house_lst[0])
# else:
#     # 이분 탐색
#     while left <= right:
#         mid = (left + right) // 2
#         # 공유기 설치 위치  최솟 값 + 중간 값
#         wifi = min(house_lst) + mid
#         count = 1
        
#         for i in range(1, len(house_lst)):
#             # 공유기 설치 위치가 집 위치보다 작거나 같을때
#             if wifi <= house_lst[i]:
#                 count += 1 # 공유기 설치
#                 wifi = house_lst[i] + mid 
                
#         # 만약 설치할 공유기가 남아있지 않다면 최솟 값을 바꿔 다시 비교
#         if count >= C:
#             left = mid + 1
#         else:
#             right = mid - 1
        
#     print(right)