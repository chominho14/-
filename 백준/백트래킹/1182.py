import sys
from itertools import combinations
input = sys.stdin.readline


n, s = map(int, input().split())

arr = list(map(int, input().split()))

# 방법2. Itertools 사용하기
cnt = 0
# 1개부터 n개까지
for i in range(1, n+1):
    for j in combinations(arr, i):
        if sum(j) == s:
            cnt += 1
print(cnt)
    


# # 방법1. 백트래킹을 이용한 방법
# cnt = 0
# k = []
# def dfs(start):
#     global cnt
    
#     # k의 길이가 0보다 작은 경우도 체크
#     if sum(k) == s and len(k) > 0:
#         cnt += 1
    
#     for i in range(start, n):
#         # 경우의 수 추가
#         k.append(arr[i])
#         # 깊이 탐색
#         dfs(i+1)
#         # 이전 상황 돌아가기
#         k.pop()
        
# # 기존에 풀었던 백트래킹은 자연수 // 이 문제는 배열이므로 0부터 시작
# dfs(0)
# print(cnt)