def solution(cap, n, deliveries, pickups):
    answer = 0
    
    # 왕복 거리의 최단 거리를 구해야 하므로 배열을 뒤집어서 구한다.
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    
    d = 0
    p = 0
    
    for i in range(n):
        # 각 집마다 수거나 배달을 추가
        d += deliveries[i]
        p += pickups[i]
        
        # 배달, 수거 할 곳이 하나라도 있으면 진행
        while d>0 or p>0:
            d -= cap
            p -= cap
            # 왕복 거리
            answer += (n - i) * 2
    return answer

