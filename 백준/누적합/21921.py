x, n = map(int, input().split())
v = list(map(int, input().split()))

s = [0]
sum_v = 0
for i in v:
    sum_v += i 
    s.append(sum_v)

result = []
for i in range(x-n+1):
    result.append(s[i+n]- s[i])

# 최대 방문자 수 출력
max_r = max(result)
if max_r == 0:
    print("SAD")
else:
    print(max_r)
    print(result.count(max_r))




   
# # -------시간 초과 ---------
# for i in range(x-n+1):
#     sum_v = 0
#     for j in range(i, i+n):
#         sum_v+=v[j]
#     s.append(sum_v)

# # 최대 방문자 수 출력
# max_s = max(s)
# if max_s == 0:
#     print("SAD")
# else:
#     print(max(s))
#     print(s.count(max(s)))
