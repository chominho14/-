arr=[]
for i in range(5):
    s1, s2, s3, s4 = map(int, input().split())
    arr.append(s1+s2+s3+s4)
print(arr.index(max(arr))+1, max(arr))