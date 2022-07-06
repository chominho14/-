
# 1. 주어진 값들과 H의 차
# 2. 그것들의 합이 최저가 되어야 함
# 3. 절단 된 나무들의 최대
# 높이를 출력

N, M = map(int, input().split())
tree_lst = list(map(int, input().split()))

# 이분 탐색
start, end = 1, max(tree_lst)
while start <= end:
    mid = (start + end) // 2
    
    # 잘린 나무들의 합을 더해 준다.
    sum = 0
    for i in tree_lst:
        if i-mid >= 0:
            sum += i-mid
    # 그 값들이 주어진 M 값보다 크면 start를 늘림
    if sum >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)