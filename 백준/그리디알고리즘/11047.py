
# 첫 줄 입력값 나누기
n, cash=input().split()
n=int(n)
cash=int(cash)

# 코인 정보들 따로 저장
coin_list=list()
for i in range(n):
    coin_list.append(int(input()))

# 코인 갯수 저장 변수
coin_cnt=0

for i in reversed(range(n)): # 코인 저장 된 리스트 끝부터 비교
    coin_cnt += cash//coin_list[i] # 몫을 코인 갯수에 누적
    cash = cash%coin_list[i] # 나머지 값을 계속 업데이트
print(coin_cnt)