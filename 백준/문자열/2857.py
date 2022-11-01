arr = []
for i in range(5):
    arr.append(input())
inFbi = False
for i in range(5):
    if "FBI" in arr[i]:
        print(i+1, end=" ")
        inFbi = True
if not inFbi:
    print("HE GOT AWAY!")