# 결국 sum_n이 대칭이 된다는 말은 reverse햇을 경우에 같으면 된다.

t = int(input())

for _ in range(t):
    n = input()
    rev_n = n[::-1]
    sum_n = int(n) + int(rev_n)
    str_sum_n = str(sum_n)
    if str_sum_n == str_sum_n[::-1]:
        print("YES")
    else:
        print("NO")


# 방법 1

# t = int(input())

# for _ in range(t):
#     n = input()
#     rev_n = n[::-1]
#     sum_n = int(n) + int(rev_n)
#     str_sum_n = str(sum_n)
#     result = True
#     for i in range(round(len(str_sum_n)/2)):
#             if str_sum_n[i] != str_sum_n[-1-i]:
#                 result = False
        
#     if result:
#         print("YES")
#     else:
#         print("NO")
