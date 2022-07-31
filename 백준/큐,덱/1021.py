from collections import deque

N, M = map(int, input().split())
opt = list(map(int, input().split()))
arr = []
# dq에 deque([1,2,3,4,...N])으로 만든다.
dq = deque([i for i in range(1, N+1)])
    
cnt = 0
# opt에 있는 것에 각각 반복문을 돌린다.
for i in opt:
    while True:
        if dq[0] == i: # dq에 첫 값과 opt의 값과 같다면
            dq.popleft()
            break
        else:
            # dq에 있는 i원소의 인덱스 값이 dq길이의 절반보다 작을 경우
            if dq.index(i) < len(dq)/2:
                while dq[0] != i:
                    dq.append(dq.popleft()) # 맨 앞에서 뒤로 값을 이동
                    cnt += 1
            else:
                while dq[0] != i:
                    dq.appendleft(dq.pop()) # 맨 뒤에있는 값을 맨 앞으로 이동
                    cnt+=1

print(cnt)