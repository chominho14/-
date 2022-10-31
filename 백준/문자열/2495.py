arr = []
for i in range(3):
    word = input()
    cnt=1
    for j in range(7):
        if word[j] == word[j+1]:
            cnt+=1
        arr.append(cnt)
        
        if word[j] != word[j+1]:
            cnt=1
    print(max(arr))
    arr=[]