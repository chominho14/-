from collections import deque

K = int(input())
dq=deque()

# 첫 값이 0이 들어갈 경우 오류 막기
dq.append(int(input()))

for _ in range(1,K):
    cash = int(input())
    
    # 0이 연속해서 들어갈 경우 막기
    if len(dq)>0:
        if cash == 0:
            dq.pop()
        else:
            dq.append(cash)
    elif len(dq)==0:
        if cash == 0:
            continue
        else:
            dq.append(cash)
      
# dq 안에 있는 모든 값을 더한다
sum = 0      
for i in range(len(dq)):
    sum += dq[i]
    
print(sum)