s = "111333344"
r = []
new_r = []
cnt = 0
for i in range(len(s)):
    if len(r) == 0 or i == 0:
        r.append(s[i])
    if len(r) >= 1:
        if s[i] == s[i-1]:
            r.append(s[i])
            print(r)
        if s[i] != r[-1] or i == len(s)-1:
            new_r.append("".join(r))
            r = []
    
            
new_r = list(map(int, new_r))
print(max(new_r))
