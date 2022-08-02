
import sys


board = dict()
check = [[0]*5 for _ in range(5)]

# board에 5x5로 값들을 넣고 위치를 부여한다.
for i in range(5):
    a = list(map(int, input().split()))
    for j in range(5):
        board[a[j]] = (i, j)

cnt = 0
for _ in range(5):
    a = list(map(int, input().split()))
    
    for i in range(5):
        cnt += 1
        
        # a[i]의 값이 board에 있으면 그 위치에 check 값을 1로 변경
        if a[i] in board:
            check[board[a[i]][0]][board[a[i]][1]] = 1
        
            # 빙고 수 세기
            bingo = 0
            # 가로 세로
            for j in range(5):
                # 가로
                if sum(check[j]) == 5:
                    bingo += 1
                # 세로
                if sum([k[j] for k in check]) == 5:
                    bingo += 1
                    
            # 대각선 \
            if check[0][0]+check[1][1]+check[2][2]+check[3][3]+check[4][4] == 5:
                bingo += 1
            # 대각선 /
            if check[0][4]+check[1][3]+check[2][2]+check[3][1]+check[4][0] == 5:
                bingo += 1
                
            if bingo >= 3:
                print(cnt)
                sys.exit()
                