
N = int(input())
A = list(map(int, input().split()))

cnt = [0] # 오큰수를 0번째 인덱스부터 확인한다.
res = [-1] * N

for i in range(1, N):

    # 오큰수가 있는지 확인한다.
    while cnt and A[cnt[-1]] < A[i]:
        # 오큰수이면 비교한 값을 팝하고 오큰수를 입력 받는다.
        # 위 과정을 오큰수 리스트가 사라질 때까지 한다.
        res[cnt.pop()] = A[i]

    # 오큰수를 비교할 인덱스를 추가한다.
    cnt.append(i)

print(*res)



# N = int(input())
# A = list(map(int, input().split()))

# s =[] 

# for i in range(N):
#     cnt = 0
#     for j in range(i+1,N):
#         if A[i] < A[j]:
#             s.append(A[j])
#             cnt+=1
#         if cnt > 0:
#             continue
    
#     if cnt == 0:
#         s.append(-1)
# print(s)