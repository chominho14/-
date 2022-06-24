# 입력된 식을 -로만 나누어 변수에 저장
s=input().split('-')

# -로 나누어진 식을 +로 계산된 값을 저장할 리스트
plus=[]

for i in s:
    cnt=0 # 더한 값을 저장
    a=i.split('+')
    for j in a: # +로 나눈 값을 모두 더해 cnt에 저장해 줌
        cnt+=int(j)
    plus.append(cnt)
    
# -로 나누어진 값들을 더한 리스트를 다시 -로 계산해 줌
result=plus[0]
for k in range(1,len(plus)):
    result-=plus[k]
print(result)