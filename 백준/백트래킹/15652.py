
# 조건문을 사용하지 않고 풀이할 수 있다.

N, M = map(int, input().split())

s = []

def dfs(start):
    if M == len(s):
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, N+1):
        s.append(i)
        dfs(i)
        s.pop()
        
        
dfs(1)



# 나의 풀이
# 반복이 되므로 좋지 않다.
# N, M = map(int, input().split())

# s = []

# def dfs():
#     if M == len(s):
#         print(' '.join(map(str, s)))
#         return
    
#     for i in range(1, N+1):
#         if len(s) >= 1:
#             if i < s[-1]:
#                 continue
#             s.append(i)
#             dfs()
#             s.pop()
#         else:
#             s.append(i)
#             dfs()
#             s.pop()
        
        
# dfs()