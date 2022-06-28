
N = int(input())
card_num = list(map(int, input().split()))

dict1 = dict()

# 숫자카드와 개수를 딕셔너리에 담기
for i in card_num:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1


M = int(input())
M_num = list(map(int, input().split()))

for i in M_num:
    if i in dict1:
        print(dict1[i], end=' ')    # 존재하는 숫자 카드라면
    else:
        print(0, end=' ')           # 존재하지 않는 숫자 카드라면
    