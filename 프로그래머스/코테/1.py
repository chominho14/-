# 1
# def day(month):
#     return month*28
# def dayChange(today):
#     toYear, toMonth, toDay = today.split('.')
#     allDay = int(toYear)*336 + int(toMonth)*28 + int(toDay)
#     return allDay

# def solution(today, terms, privacies):
#     answer = []
#     colToday = dayChange(today)
#     dic = dict()
#     for t in terms:
#         term, tMonth = t.split()
#         tMonth = int(tMonth)
#         dic[term] = day(tMonth)

#     for i in range(len(privacies)):
#         priDay, priTerm = privacies[i].split()
#         if colToday >= dayChange(priDay) + dic[priTerm]:
#             answer.append(i+1)

#     return answer


# 5
# def updateOne(r, c, value, graph):
#     r = int(r)
#     c = int(c)
#     graph[r][c] = value

# def updateTwo(value1, value2, graph):
#     for i in range(51):
#         for j in range(51):
#             if graph[i][j] == value1:
#                 graph[i][j] = value2

# def merge(r1, c1, r2, c2, graph):
#     r1 = int(r1)
#     c1 = int(c1)
#     r2 = int(r2)
#     c2 = int(c2)
#     graph[r2][c2] = graph[r1][c1]

# def unMerge(r, c, graph):
#     r = int(r)
#     c = int(c)
#     temp = graph[r][c]
#     updateTwo(graph[r][c], "", graph)
#     updateOne(r, c, temp, graph)

# def solution(commands):
#     answer = []
#     graph = [[""]*51 for _ in range(51)]

#     for i in commands:
#         command = list(map(str, i.split()))
#         if command[0] == 'UPDATE':
#             if len(command) == 4:
#                 updateOne(command[1],command[2],command[3],graph)
#             else:
#                 updateTwo(command[1],command[2],graph)
#         elif command[0] == "MERGE":
#             merge(command[1],command[2],command[3],command[4],graph)
#         elif command[0] == "UNMERGE":
#             unMerge(command[1],command[2],graph)
#         else:    
#             loc = graph[int(command[1])][int(command[2])]     
#             if loc == "":
#                 answer.append("EMPTY")
#             else:
#                 answer.append(loc)

#     return answer

# 2
# def solution(cap, n, deliveries, pickups):
#     result = 0
#     while sum(deliveries)!=0 and sum(pickups)!=0:
#         deliCap = cap
#         pickCap = cap
#         for i in range(n-1, -1, -1):
#             if deliveries[i] > 0 and deliCap > 0:
#                 if deliveries[i] > deliCap:
#                     deliveries[i] = deliveries[i] - deliCap
#                     deliCap = 0
#                 else:
#                     deliveries[i] = 0
#                     deliCap = deliCap - deliveries[i]
#             result += i+1
#             if pickups[i] > 0 and pickCap > 0:
#                 if pickups[i] > pickCap:
#                     pickups[i] = pickups[i] - pickCap
#                 else:
#                     pickups[i] = 0
#                     pickCap = pickCap - pickups[i]
#     return result

