v = int(input())
i = input()
cnt = 0
for k in i:
    if k=="A":
        cnt+=1
v2 = v/2
if cnt>v2:
    print("A")
elif cnt<v2:
    print("B")
else:
    print("Tie")