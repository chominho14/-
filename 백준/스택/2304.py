n = int(input())

pillar = [[] for _ in range(n)]


for i in range(n):
    l, h = map(int, input().split())
    
    pillar[i].append(l)
    pillar[i].append(h)

# 기둥들을 정렬
pillar.sort()

# 가장 큰 값 찾기, 위치 저장
temp = 0
temp_i = 0
for i in range(n):
    if temp < pillar[i][1]:
        temp = pillar[i][1]
        temp_i = i+1
        
st_l = [0]
st_r = [0]

left = pillar[0][0]
right = pillar[n-1][0]

# 가장 큰 기둥 바로 전까지 기둥들을 비교하며 왼쪽 스택에 저장
for i in range(left, pillar[temp_i-1][0]):
    flag_l = True
    # 하나하나 비교해주기
    for j in range(temp_i-1):        
        if i == pillar[j][0]:    
            if pillar[j][1] > st_l[-1]:
                st_l.append(pillar[j][1])
                flag_l = False
                
    if flag_l:
        st_l.append(st_l[-1])

# 오른쪽에서 가장 큰 기둥까지 다가와주기
for i in range(right+1, pillar[temp_i-1][0], -1):
    flag_r = True
    for j in range(temp_i, n):        
        if i == pillar[j][0]:    
            if pillar[j][1] > st_r[-1]:
                st_r.append(pillar[j][1])
                flag_r = False
                
    if flag_r:
        st_r.append(st_r[-1])
        
# 스택에 저장된 것들과 가장 긴 기둥의 값 더하기
result = 0
result = sum(st_l) + sum(st_r) + temp

print(result)


