arr = []
temp=0
for _ in range(4):
    arr_out, arr_in = map(int, input().split())
    temp += arr_in - arr_out
    arr.append(temp)

print(max(arr))