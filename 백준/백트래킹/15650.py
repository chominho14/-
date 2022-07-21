N, M = map(int, input().split())

# 스택을 채울 리스트
s = []

def dfs(start):
    # 값을 찾았으면 출력
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, N + 1):
        # 값이 중복이라면 배제
        if i in s:
            continue
        # 해당 경우의 수 추가
        s.append(i)
        # 깊이 탐색 동작
        dfs(i)
        # 이전 상황 돌아가기
        s.pop()
        
dfs(1)