f = input()

st = []


for i in f:
    if i == "+":
        st.append(st.pop()+st.pop())
    elif i == "-":
        a = st.pop()
        b = st.pop()
        st.append(b-a)
    elif i == "*":
        st.append(st.pop()*st.pop())
    elif i == "/":
        a = st.pop()
        b = st.pop()
        st.append(b//a)
    else:
        st.append(int(i))

print(st[0])