check = ['a','e','i','o','u','A','E','I','O','U']
while True:
    cnt = 0
    sentence = input()
    if sentence == "#":
        break
    for i in range(len(sentence)):
        if sentence[i] in check:
            cnt += 1
    print(cnt)
    