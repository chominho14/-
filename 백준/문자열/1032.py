n = int(input())

result = []
arr = []

for i in range(n):
    word = input()
    for j in word:
        arr.append(j)
    if len(result)==0:
        result = arr
    if len(result)>0:
        for k in range(len(arr)):
            if result[k]!=arr[k]:
                result[k] = "?"
    arr = []
print("".join(result))