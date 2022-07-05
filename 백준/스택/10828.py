import sys
n = int(sys.stdin.readline())

stack=[]
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0]=='push':
        stack.append(command[1])
    elif command[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
            
            
            
# 아래와 같이 코딩하면 시간 초과...

# from collections import deque

# N = int(input())
# dq = deque()
# result=[]

# for _ in range(N):
#     command = input()
#     if 'push' in command[0]:
#         _, num = command.split(' ')
#         dq.append(num)
#     elif 'top' in command:
#         if len(dq)==0:
#             result.append(-1)
#         else:
#             result.append(dq[-1])
#     elif 'size' in command:
#         result.append(len(dq))
#     elif 'empty' in command:
#         if len(dq)==0:
#             result.append(1)
#         else:
#             result.append(0)
#     elif 'pop' in command:
#         if len(dq)==0:
#             result.append(-1)
#         else:
#             result.append(dq[-1])
#             dq.pop()

# for i in range(len(result)):
#         print(result[i])


    