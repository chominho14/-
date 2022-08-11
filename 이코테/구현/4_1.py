N = int(input())

prov = list(map(str, input().split()))
X = 0
Y = 0
for i in prov:
    if i == "L":
        if Y > 0:
            Y -= 1
    elif i == "R":
        if Y < N-1:
            Y += 1
    elif i == "U":
        if X > 0:
            X -= 1
    elif i == "D":
        if X < N-1:
            X += 1

print(X+1, Y+1)