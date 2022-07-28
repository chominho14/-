
# 덱 사용
from collections import deque
 
T = int(input())
 
for i in range(T):
    p = input()
    n = int(input())
    # 제공된 배열 모양의 문자열을 배열로 만들어 준다.
    xArr = input()[1:-1].split(',') 
    dq = deque(xArr)
    # 배열을 매번 뒤집지 않고 R이 홀수일 때만 뒤집는다.
    flag = 0
 
    if n == 0:
        dq = []
 
    for j in p:
        if j == 'R':
            flag += 1
        elif j == 'D':
            if len(dq) == 0:
                print("error")
                break
            else:
                # 만약 R이 짝수면 앞에서 제거, 홀수면 뒤에서 제거
                if flag % 2 == 0:
                    dq.popleft()
                else:
                    dq.pop()
 
    else:
        if flag % 2 == 0:
            print("[" + ",".join(dq) + "]")
        else:
            # 마지막에만 뒤집어 준다.
            dq.reverse()
            print("[" + ",".join(dq) + "]")




# 런타임 에러 코드

# T = int(input())

# for i in range(T):
#     p = input()
#     n = int(input())
#     cnt = 0
#     for j in range(len(p)):
#         if p[j] == "D":
#             cnt += 1
#     if cnt > n:
#         print("error")
#         continue
#     else:
#         xArr = input()
#         newXArr = list(map(int,xArr[1:-1].split(",")))
#         for k in range(len(p)):
#             if p[j] == "R":
#                 newXArr.reverse()
#             elif p[j] == "D":
#                 newXArr.pop(0)
            
#         print("[", end="")
#         for r in range(len(newXArr) - 1):
#             print("%d,"%newXArr)
#         print(newXArr[-1],end="")
#         print("]")
        


