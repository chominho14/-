word = list(input())

for i in range(len(word)):
    k = ord(word[i]) - 3
    if k < ord('A'):
        k += 26
    word[i] = chr(k)
    
print(''.join(word))