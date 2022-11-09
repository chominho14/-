n=int(input())
result=[]
for i in range(n):
    name, score = input().split()
    result.append([name,int(score)])
# 람다 함수를 이용하여 하나는 오름차순, 하나는 내림 차순으로 정리
result.sort(key=lambda x: (-x[1],x[0]))
print(result[0][0])