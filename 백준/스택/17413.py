s = input()

st = []
flag = False

st_r = []

for i in s:
    if i == '<':
        flag = True
        if st_r:
            st.extend(reversed(st_r))
        st.append(i)
    
    elif i == '>':
        flag = False
        if st_r:
            st_r.clear()
        st.append(i)

    else:
        if flag:
            st.append(i)
        else:
            if i == ' ':
                if st_r:
                    st.extend(reversed(st_r))
                    st_r.clear()
                    st.append(i)
            else:
                st_r.append(i)

if st_r:
    st.extend(reversed(st_r))

print(''.join(st))



