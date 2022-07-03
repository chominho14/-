

N=int(input())
human_info=[]

# 리스트에 몸무게와 키를 담는다
for _ in range(N):
    w, h = list(map(int, input().split()))
    human_info.append((w,h))
    
# 리스트에 모든 값들과 비교
for i in human_info:
    rank = 1
    # 몸무게와 키 둘 다 작다면 랭크 + 1
    for j in human_info:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")