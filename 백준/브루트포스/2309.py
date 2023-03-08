result = []

for _ in range(9):
    result.append(int(input()))

# 오름차순
result.sort()
    
# 방법1. 9개 중에 7개를 뽑는 것
# 모르겠음.

# 방법2. 9개 중에 2개를 뽑아 모든 합에서 뺀 것이 100인 것

sum_result = sum(result)
index = []

for i in range(8):
    for j in range(i+1, 9):
        sum_two = 0
        sum_two = result[i] + result[j]
        if(sum_result - sum_two == 100):
            index.append([i,j])

# 정답이 여러가지인 경우에 아무거나 출력이므로 가장 처음 값 출력
result.pop(index[0][0])
result.pop(index[0][1]-1)
for i in range(7):
    print(result[i])
    
    
# 파이썬에는 순열과 조합 라이브러리를 제공한다
# itertools

# import itertools
# array = [int(input()) for _ in range(9)]
# for i in itertools.combinations(array, 7):

# 위의 코드를 이용하여 9개 중 7개를 중복 없이 뽑을 수 있다.