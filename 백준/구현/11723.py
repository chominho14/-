
# set 함수를 이용하여 처리하는 것이 포인트
# 특히 discard로 제거해주는 것이 포인트
import sys

m = int(sys.stdin.readline())

arr = set()
for i in range(m):
    inp = sys.stdin.readline().split()
    if len(inp)==1:
        if inp[0]=="all":
            arr = set([i for i in range(1,21)])
        else:
            arr = set()
    else:
        trans, num = inp[0],inp[1]
        num=int(num)
        if trans=="add":
            arr.add(num)
        elif trans=="check":
            if num in arr:
                print(1)
            else:
                print(0)
        elif trans=="remove":
            if num in arr:
                arr.discard(num)
        else:
            if num in arr:
                arr.discard(num)
            else:
                arr.add(num)

            


# 배열로 하면 시간 초과가 뜬다.
# arr = []
# for _ in range(m):
#     inp = input()
#     if inp=="all":
#         arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#     elif inp=="empty":
#         arr.clear()
#     else:
#         trans, num = map(str, inp.split())
#         if trans=="add":
#             if num not in arr:
#                 arr.append(num)
#         elif trans=="check":
#             if num in arr:
#                 print(1)
#             else:
#                 print(0)
#         elif trans=="remove":
#             if num in arr:
#                 arr.remove(num)
#         else:
#             if num in arr:
#                 arr.remove(num)
#             else:
#                 arr.append(num)
            