t=int(input())

for _ in range(t):
    yonsei=0
    korea=0
    for _ in range(9):
        a, b = map(int, input().split())
        yonsei+=a
        korea+=b
    
    if yonsei > korea:
        print("Yonsei")
    elif yonsei < korea:
        print("Korea")
    else:
        print("Draw")