word=input()
t_f = True
for i in range(3):
    if word[i]!="5":
        t_f=False
if t_f:
    print("YES")
else:
    print("NO")