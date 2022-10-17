n = int(input())
for i in range(n):
    password = input()
    if 6 <= len(password) <= 9:
        print("yes")
    else:
        print('no') 