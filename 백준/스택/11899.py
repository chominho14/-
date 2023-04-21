s = input()

st = []
cnt = 0

for i in range(len(s)):
    if s[i] == ")":
        if st:
            st.pop()
        else:
            cnt += 1
    else:
        st.append(s[i])

print(cnt + len(st))