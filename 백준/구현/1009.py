t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    a = a%10
    
    # a가 0이면 10의 거듭제곱
    if a == 0:
        print(10)
    elif a==1 or a==5 or a==6: # 1,5,6은 매번 자기 자신이 나옴
        print(a)
    elif a==4 or a==9: # 거듭제곱을 10으로 나눈 나머지가 두 가지 경우
        b = b%2
        if b==0:
            print(a*a%10)
        else:
            print(a)
    else: # 4가지 경우의 거듭 제곱은 b가 4의 배수일 경우만 최적화
        b=b%4
        if b==0:
            print(a**4%10)
        else:
            print(a**b%10)

# 시간 초과
# for _ in range(t):
#     a, b = map(int, input().split())
#     print((a**b)%10)