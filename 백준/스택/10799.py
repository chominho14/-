bracket = input()

s = []
result = 0

for i in range(len(bracket)):
    
    if bracket[i] == '(':
        s.append(bracket[i])
    
    if bracket[i] == ')':
        if bracket[i-1] == '(':
            s.pop()
            result += len(s)
        else:
            s.pop()
            result += 1
    
print(result)