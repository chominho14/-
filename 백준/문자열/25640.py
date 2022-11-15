word=input()
n=int(input())
cnt=0
for i in range(n):
    input_word=input()
    if word==input_word:
        cnt+=1
        
print(cnt)