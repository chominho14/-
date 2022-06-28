
n_num = int(input())
a_lst = list(map(int, input().split()))
a_lst.sort()

m_num = int(input())
m_lst = list(map(int, input().split()))


# 이분 탐색    
for i in m_lst:
    left, right = 0, n_num-1 # 맨 앞(left), 맨 뒤(right)
    result=False # m_lst에 값이 있으면 True, 없으면 False
    
    # 이분 탐색 시작
    while left <= right: # left가 right보다 커지면 탈출
        mid = (left + right) // 2 # left와 right의 중간 값
        if i == a_lst[mid]: # m_lst의 값과 탐색 값이 같을 때
            result = True # m_lst에 결과 값 존재
            print(1) # 1 출력
            break
        
        elif i > a_lst[mid]: # m_lst의 값이 a_lst값보다 클 때
            left = mid + 1 # left를 높임
        else:
            right = mid - 1
    
    if not result:
        print(0)
    
    