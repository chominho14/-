# 자료구조를 최대한 활용
# 커서를 기준으로 배열 두개를 사용하여 구한다.
import sys

n_l = list(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline())

n_r = []

for _ in range(m):
    order = list(sys.stdin.readline().split())
    
    if order[0] == 'L':
        if n_l:
            n_r.append(n_l.pop())
    
    elif order[0] == 'D':
        if n_r:
            n_l.append(n_r.pop())
    
    elif order[0] == 'B':
        if n_l:
            n_l.pop()
    
    else:
        n_l.append(order[1])

n_l.extend(reversed(n_r))
print(''.join(n_l))


# 시간 초과 - 시간제한 0.3초


# n = input()
# m = int(input())
# cursor = len(n)

# for _ in range(m):
#     order = input()    
    
#     if order == 'L':
#         if cursor != 0:
#             cursor -= 1
    
#     elif order == 'D':
#         if cursor != len(n):
#             cursor += 1
    
#     elif order == 'B':
#         n = n[:cursor] + n[cursor+1:]
#         cursor -= 1
    
#     else:
#         _, s = map(str, order.split())
        
#         n = n[:cursor] + s + n[cursor:]
#         cursor += 1
# print(n)