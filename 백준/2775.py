T = int(input())

for _ in range(T):
    k=int(input()) # 층 수
    n=int(input()) # 호 수
    people = [i for i in range(1, n+1)] # 호에 따른 사람들
    
    for _ in range(k): # 층 수 증가
        # 1호부터 b호까지 값 누적
        for j  in range(1,n): 
            people[j] += people[j-1]
    print(people[-1])