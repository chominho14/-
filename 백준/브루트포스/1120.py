a, b = map(str, input().split())

# 여러 결과 값
result = []

# a를 b의 처음부터 통으러 넣어 비교
for i in range(len(b)-len(a)+1):
    cnt = 0
    # a와 b 를 비교하여 다르다면 cnt 증가
    for j in range(len(a)):
        if a[j] != b[i+j]:
            cnt += 1
    result.append(cnt)

# 결과 값 중 최솟 값 출력
print(min(result))