n = int(input())
result = []     # +,- 결과값 저장
s = []          # 1,2,3,4,... 저장
no_data = True  # 수열 불가할 경우
cnt = 0


for i in range(n):
    data = int(input())
    # cnt가 data와 같아질때까지 반복
    while cnt < data:
        cnt += 1
        s.append(cnt)
        result.append("+")
    
    # data와 수열이 같으면 pop, - 추가
    if s[-1] == data:
        s.pop()
        result.append("-")
    else:
        no_data = False
        continue

# 만약 수열이 이루어지지 않는다면 NO 출력
if no_data == False:
    print("NO")
else:
    print("\n".join(result))
        