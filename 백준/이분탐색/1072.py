
X, Y = map(int, input().split())

# (Y//X) * 100 은 오류
per = (Y*100) // X

# 확률이 99이상이면 -1 출력
if per >= 99:
    print(-1)
else:
    result = 0
    start = 1
    end = X

    # 이분탐색 시작
    while start <= end:
        mid = (start + end) // 2
        
        # 만약 per이 mid를 더해 구해진 승률보다 낮다면 값을 결과에 넣고 끝을 mid - 1로
        if per < ((Y+mid)*100 //(X+mid)):
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    print(result)
    