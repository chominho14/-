t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    n_arr = list(map(int, input().split()))
    m_arr = list(map(int, input().split()))
    
    n_arr.sort()
    m_arr.sort()
    
    n_arr_p = 0
    
    m_arr_p = 0
    cnt = 0
    
    while n_arr_p < n and m_arr_p < m:
        
        if n_arr[n_arr_p] <= m_arr[m_arr_p]:
            n_arr_p += 1
        
        else:
            cnt += n - n_arr_p
            m_arr_p += 1

        
    print(cnt)