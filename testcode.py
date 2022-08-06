N = int(input())

cnt = 0

for i in range(N):
    word = input()
    
    err = 0
    for k in range(len(word)-1):
        
        if word[k] != word[k+1]:
            new_word = word[k+1:]
            
            if new_word.count(word[k]) > 0:
                err += 1
    
    if err == 0:
        cnt += 1

print(cnt)
                