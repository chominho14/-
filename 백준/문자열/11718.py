
while True:
    try:
        print(input())
    except EOFError: # 입력이 끝났을 경우
        break