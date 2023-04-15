from collections import deque

# deque를 사용하여 손쉽게 구현하자!
n = int(input())

q = deque(map(int, input().split()))
s = deque()

i = 1

while q:
    if q[0] == i:
        q.popleft()
        i += 1
    else:
        s.append(q.popleft())
        
    while s and s[-1] == i:
        s.pop()
        i += 1

if s:
    print("Sad")
else:
    print("Nice")


   
# 단순 구현으로 풀어보려했으나 91%에서 틀림    

# n = int(input())
# stu = list(map(int, input().split()))

# stu.reverse()
# s = []
# result = [0]

# k = 1
     
# for i in range(n-1, -1, -1):
    
#     if stu[i] == k:
#         result.append(stu[i])
#         k += 1
#     else:
#         if s:
#             for j in range(len(s)-1, -1 , -1):
#                 if s[j] == k:
#                     result.append(s.pop())
#                     k += 1
                
#             s.append(stu[i])
                    
#         else:
#             s.append(stu[i])

# if s:
#     for j in range(len(s)-1, -1 , -1):
#         if s[j] == k:
#             result.append(s.pop())
#             k += 1
 

# if result[-1] == n:
#     print("Nice")
# else:
#     print("Sad")
    