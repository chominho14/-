
# 1번 문제
# X = "100"
# Y = "2345"

# def solution(X, Y):
#     answer = ''
    
#     xArr = sorted(list(map(int, X)))
#     yArr = sorted(list(map(int, Y)))
    
    
#     result = []
#     i = 0
#     j = 0
#     k = 0
#     while i < len(X) and j < len(Y):
#         if xArr[i] < yArr[j]:
#             i += 1
#         elif xArr[i] > yArr[j]:
#             j += 1       
#         else:
#             result.append(xArr[i])
#             i += 1
#             j += 1    

#     result.sort(reverse=True)
#     answer = "".join([str(_) for _ in result])
    
#     if len(result) == 0:
#         return "-1"
#     elif result.count(0) == len(result):
#         return "0"
#     else:
#         return str(answer)

# solution(X, Y)


# 2번 문제
# 16점...
# def solution(want, number, discount):
#     answer = 0
#     numSum = sum(number)

#     for i in range(len(discount)-numSum):
#         cnt = 0
#         k = 0
#         for j in range(numSum):
#             if discount[i+k] in want:
#                 cnt += 1
#             k += 1
#         if cnt == numSum:
#             answer += 1

#     return answer