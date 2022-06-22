
n=int(input())
# 공백으로 들어온 값을 int타입으로 리스트로 만들어 준다.
s=list(map(int, input().split()))
print(s)
num=0

# 오름차순으로 정렬
s.sort()

# 합을 계속 더하는 과정
for i in range(n):
    for j in range(i+1):
        num += s[j]
print(num)