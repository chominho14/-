n = int(input())
for _ in range(n):
    sentence = list(input())
    for i in range(len(sentence)):
        if i == 0:
            sentence[i] = sentence[i].upper()
    print("".join(sentence))


# 한 줄로 줄이기도 가능    
# sentence = sentence[0].upper() + sentence[1:]
