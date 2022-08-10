from itertools import combinations

# 모음 정리
vowels = ('a','e','i','o','u')

L, C = map(int, input().split())

prov = input().split(" ")
prov.sort() # 증가하는 순서로 배열 되므로

# L개 만큼의 조합을 뽑는다.
for password in combinations(prov, L):
    cnt = 0
    for i in password:
        # 모음이 있다면 cnt 증가
        if i in vowels:
            cnt += 1
    # 계산 결과가 모음이 1개 이상 자음이 2개 이상이면 출력
    if cnt >= 1 and cnt <= L - 2:
        print("".join(password))
    