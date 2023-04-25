p = 0

while True:
    s = input()
    st = []
    
    cnt = 0
    
    if s[0] == "-":
        break
    
    for i in range(len(s)):
        if s[i] == "{":
            st.append(s[i])
            
        else:
            if st:
                st.pop()
            else:
                cnt += 1
                st.append("{")
        
    p += 1
    cnt += len(st)//2
    
    
    
    print(f'{p}. {cnt}')
    