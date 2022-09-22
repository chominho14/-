word = input()
vowel=['a','e','i','o','u']

cnt = 0
for i in range(len(word)):
    if word[i] in vowel:
        cnt+=1
    
print(cnt)