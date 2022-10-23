n, m = map(int, input().split())

print((str(n)*n)[:m])


# 풀이 1 . (출력 초과)
# pri = []
# for i in str(n):
#     pri.append(i)

# result = []
# for _ in range(n):
#     for i in pri:
#         result.append(i)

# if len(result) <= m:
#     for i in result:
#         print(i, end="")
# else:
#     for i in range(m):
#         print(result[i],end="")