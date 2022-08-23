N = int(input())

arr = []
for i in range(N):
    a = input()
    arr.append(a)

arr_1 = list(set(arr))

arr_1.sort()
arr_1.sort(key=len)

for i in arr_1:
    print(i)