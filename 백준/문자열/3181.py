word=list(map(str, input().split()))
skip=['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
for i in range(len(word)):
    if i==0 or (word[i] not in skip):
        print(word[i][0].upper(), end="")