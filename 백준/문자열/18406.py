word = input()

len_word=len(word)//2
left=0
right=0
for i in range(len_word):
    left+=int(word[i])
    right+=int(word[len_word+i])
if left==right:
    print("LUCKY")
else:
    print("READY")