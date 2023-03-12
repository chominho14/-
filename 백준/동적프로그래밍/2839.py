n = int(input())

# 연산 횟수
cnt=0
while n>=0:
    # 5로 나누어 지면 cnt에 나누어진 몫을 더한다.
    if n%5 == 0:
        cnt += n//5
        break
    
    # 5로 나누어지지 않았다면 3을 뺀 뒤 cnt 증가
    n -= 3
    # 만약 3과 5의 배수들로 값이 안 나올 경우
    if n<0:
        cnt = -1
        break
    cnt += 1
print(cnt)