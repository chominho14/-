
N = int(input())
A = list(map(int, input().split()))
dp = [0] # 결과 수열 저장

for i in range(N):
    low = 0
    high = len(dp) - 1

    # 이진 탐색 시작
    while low <= high:
        mid = (low + high) // 2
        
        # 결과 리스트에 있는 값이 A[i] 값보다 작을 경우 이분 탐색
        if dp[mid] < A[i]:
            low = mid + 1
        else:
            high = mid - 1

    # 기존에 없는 큰 값이면 추가해 준다.
    if low >= len(dp):
        dp.append(A[i])
    # 최솟 값이면 앞에 추가해 준다.
    else:
        dp[low] = A[i]

print(len(dp) - 1)
