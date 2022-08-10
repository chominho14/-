s = "111333344"
r = []
new_r = []
cnt = 0
for i in range(len(s)):
    if len(r) == 0 or i == 0:
        r.append(s[i])
    else:
        if s[i] == r[-1]:
            r.append(s[i])
            print(r)
        else:
            new_r.append("".join(r))
            r = []
            

print(new_r)
