# 처음으로 혼자 푼 이분탐색 문제!!!


K, N = map(int, input().split())
K_lst = []
for _ in range(K):
    K_lst.append(int(input()))

# 모두 더한다.
sum = 0
for i in K_lst:
    sum += i

# 모두 더한 값을 N으로 나눈다.
num = sum // N

# 이분탐색
start, end = 1, num
while start <= end:
    mid = (start + end) // 2
    
    # k를 mid 값으로 나눈 값들을 더하여 cnt에 저장
    cnt=0
    for i in range(K):
        cnt += K_lst[i]//mid
        
    # cnt 값이 N보다 크거나 같으면 값으로 허용
    if cnt >= N:
        start = mid + 1
        result = mid
    else: # 아니면 더 작은 값 필요
        end= mid - 1
        
print(result)
        

# 각 수들을 나눈 몫의 함이 N과 같으면 그 수 출력

