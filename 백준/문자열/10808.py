word = input()

result = [0] * (26)

for i in word:
    # ord함수를 통해 문자열을 아스키 코드로 변환
    result[ord(i) - 97] += 1

for i in result:
    print(i, end=' ')
        
