N = int(input())
idx = list(map(int, input().split()))
M = int(input())
prov = list(map(int, input().split()))

idx.sort()


for i in range(M):
    check = 0
    start = 0
    end = N - 1
    # 이진 탐색 시작
    while start <= end:
        mid = (start + end) // 2
        
        # 값을 찾으면 check를 1로 만든 뒤 break
        if prov[i] == idx[mid]:
            check = 1
            break
        # 제공된 값이 더 작다면 끝을 mid - 1로
        elif prov[i] < idx[mid]:
            end = mid - 1
        else: # 아니면 시작을 mid + 1로
            start = mid + 1
        
    print("%d"%check, end=" ")