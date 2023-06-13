# 풀이 포인트
# 반복문 마지막에 자기 자신을 스택에 추가한 뒤
# while문을 통해 자기 자신보다 작은 쓸모없는 탑들을 제거해줘야 된다.

n = int(input())
top = list(map(int, input().split()))


st = []
result = []
st.append([0, top[0]])

for i in range(n):
    
    while st:
        if st[-1][1] > top[i]:
            result.append(st[-1][0]+1)
            break
        else:
            st.pop()
        
    if not st:
        result.append(0)
    st.append([i, top[i]])

print(' '.join(map(str, result)))
    




# 시간초과
# result = [0]

# for i in range(1, len(top)):
#     temp = 0
#     for j in range(0, i):
#         if top[j] >= top[i]:
#             temp = j+1
    
#     result.append(temp)

# for i in result:
#     print(i, end=" ")
    