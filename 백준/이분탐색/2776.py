t = int(input())

for _ in range(t):
    n = int(input())
    n_arr = list(map(int, input().split()))
    n_arr.sort()
    m = int(input())
    m_arr = list(map(int, input().split()))
    for i in m_arr:
        start = 0
        end = n - 1
        result = 0
        while start <= end:
            mid = (start + end) // 2
            
            if n_arr[mid] == i:
                result = 1
                break
            elif n_arr[mid] > i:
                end = mid - 1
            else:
                start = mid + 1
        print(result)