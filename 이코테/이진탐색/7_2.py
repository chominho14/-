# 부품 찾기

N = int(input())
my_arr = list(map(int, input().split()))
M = int(input())
prov_arr = list(map(int, input().split()))

my_arr.sort()
start = 0
end = N-1
def binary_search(my_arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if my_arr[mid] == target:
            return mid
        elif my_arr[mid] > target:
            mid = end - 1
        else:
            mid = start + 1
    return None

for i in prov_arr:
    result = binary_search(my_arr, i, start, end)
    if result != None:
        print("yes",end=" ")
    else:
        print("no", end=" ")