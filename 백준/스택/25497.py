n = int(input())
skill = input()

skill_s = []
skill_l = []

num = ["1","2","3","4","5","6","7","8","9"]

cnt = 0

for i in skill:
    if i in num:
        cnt += 1
    elif i == "S":
        skill_s.append(i)
    elif i == "L":
        skill_l.append(i)
    elif i == "R":
        if skill_l:
            cnt += 1
            skill_l.pop()
        else:
            break
    elif i == "K":
        if skill_s:
            cnt += 1
            skill_s.pop()
        else:
            break
print(cnt)