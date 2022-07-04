
N = int(input())
cnt=0
plus=666

while True:
    # 666부터 하나씩 증가한 값에 666이 들어있다면 카운트 증가
    if '666' in str(plus):
        cnt+=1
    # 증가한 카운트 값이 입력 값과 같다면 반복문 탈출
    if cnt == N:
        break
    plus+= 1
    
print(plus)