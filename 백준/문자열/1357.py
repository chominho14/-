x, y = map(str, input().split())

def rev(k):
    return int(k[::-1])

print(rev(str(rev(x)+rev(y))))
    

