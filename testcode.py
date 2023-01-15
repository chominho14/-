

def solution(n, quests):
    graph = [[] for _ in range(n+1)]
    for i in range(len(quests)):
        u, v = quests[i]
        graph[v].append(u)
        

    print(graph)
    visited = [False] * (n+1)
    cnt = 1
    result=[]
    re_num = []
    for i in range(1,n+1):
        if len(re_num)==0:
            print(visited)
            if not visited[i]:
                if len(graph[i]) == 0:
                    result.append(i)
                    visited[i] = True
                else:
                    for j in range(len(graph[i])):
                        if not visited[j]:
                            re_num.append(i)
                            break
        else:
            for k in re_num:
                check_p=True
                for l in range(len(graph[k])):
                    if not visited[l]:
                        check_p=False
                if check_p:
                    visited[k]=True
    print(result)
                    






# s = "111333344"
# r = []
# new_r = []
# cnt = 0
# for i in range(len(s)):
#     if len(r) == 0 or i == 0:
#         r.append(s[i])
#     if len(r) >= 1:
#         if s[i] == s[i-1]:
#             r.append(s[i])
#             print(r)
#         if s[i] != r[-1] or i == len(s)-1:
#             new_r.append("".join(r))
#             r = []
    
            
# new_r = list(map(int, new_r))
# print(max(new_r))

