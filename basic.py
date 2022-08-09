# 리스트 컴프리핸션
# n x m 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)]

# ------------------ -------------------------- --------------

# 특정 값의 원소 지우기
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]



# ------------------ -------------------------- --------------

# 정렬, 이진 탐색, 최단경로 입력 빨리 받기
import sys
sys.stdin.readline().rstrip()


# ------------------ -------------------------- --------------

# 필수 라이브러리 6가지

# 1. 내장함수
sum()
min()
max()
eval() # 수식이 문자열로 들어올 경우
sorted([1,2,3])
sorted([1,2,3], reverse=True)
# 리스트의 원소로 리스트나 튜플 정렬하는 법
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key = lambda x:x[1], reverse = True)


# ------------------ 

# 2. itertools
# 리스트와 같은 이터러블 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우를 계산
from itertools import permutations 
result = list(permutations(data, 3))
# 리스트와 같은 이터러블 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(순열)을 계산
from itertools import combinations
result = list(combinations(data, 2))


# ------------------ 

# 3. heapq
import heapq
heapq.heappush() # 힙에 원소 삽입
heapq.heappop() # 힙에 원소 꺼내기

# 시간 복잡도 O(NlogN)에 오름차순 정렬
def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return(result)

# 내림차순 정렬
def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return(result)

# ------------------ 

# 4. bisect
# 이진 탐색 구현 - 정렬된 배열에서 특정한 원소를 찾기
from bisect import bisect_left, bisect_right
bisect_left(a, 4)
bisect_right(a, 4)
# 정렬된 리스트 값이 범위 안에 속하는 데이터 갯수 반환 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index




# ------------------ -------------------------- --------------

# 5. collections

# deque 사용해 큐 구현
from collections import deque

# Counter (원소별 등장 횟수 세기)
from collections import Counter
counter = Counter(['red'])
counter['red']
dict(counter) # 사전 자료형으로 변환 가능



# ------------------ -------------------------- --------------


# 6. math
# 팩토리얼, 제곱근, 최대공약수 등
import math
math.factorial(5) # 팩토리얼
math.sqrt(7) # 제곱근
math.gcd(21, 14) # 최대 공약수
math.pi
math.e


# ------------------ -------------------------- --------------


