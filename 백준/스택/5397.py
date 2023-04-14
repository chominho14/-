t = int(input())

for _ in range(t):
    password = input()
    cursor_l = []
    cursor_r = []
    
    for i in range(len(password)):
        
        if password[i] == "<":
            if cursor_l:
                cursor_r.append(cursor_l.pop())
        elif password[i] == ">":
            if cursor_r:
                cursor_l.append(cursor_r.pop())
        elif password[i] == "-":
            if cursor_l:
                cursor_l.pop()
        else:
            cursor_l.append(password[i])
            
    if cursor_r:
        cursor_l.extend(reversed(cursor_r))
    
    print(''.join(cursor_l))
    