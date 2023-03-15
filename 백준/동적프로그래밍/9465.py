t = int(input())

for _ in range(t):
    n = int(input())
    
    # 윗줄과 아랫줄을 나누어 그 열까지 최댓값을 저장한다.
    n_t = list(map(int, input().split()))
    n_b = list(map(int, input().split()))
    
    # n=1일 경우는 아래 for문 인덱스 에러
    if n>1:
        n_t[1] += n_b[0]
        n_b[1] += n_t[0]
    
    # 위는 대각선 아래, 두번째 대각선 아래 중 더했을 경우 가장 최대가 되는 값 저장
    for i in range(2, n):
        n_t[i] += max(n_b[i-1], n_b[i-2])
        n_b[i] += max(n_t[i-1], n_t[i-2])
    
    # 아래나 위 중 더 큰 결과 값 출력
    print(max(n_t[n-1], n_b[n-1]))
    
