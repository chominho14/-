# 갯수 입력
T = int(input())
# '(',')' 를 입력받음
s = []
for _ in range(T):
    s.append(input())
    
for i in range(T):
    cnt = 0 # 스택을 생각하여 카운터
    for j in range(len(s[i])):
        if cnt >= 0: # 0 보다 클때만 카운터 발동
            if s[i][j] == "(":
                cnt += 1
            else:
                cnt -= 1
        else: # 0보다 작으면 반복문에서 탈출
            continue
    # 만약 cnt가 0이면 참, 아니면 거짓
    if cnt == 0:
        print("YES")
    else:
        print("NO")