# temp //= 2
# temp //= 3 과정 이해하기

s = list(input())
st = []
temp = 1
result = 0

for i in range(len(s)):
    if s[i] == "(":
        st.append(s[i])
        temp *= 2
        
    elif s[i] == "[":
        st.append(s[i])
        temp *= 3
    
    elif s[i] == ")":
        if not st or st[-1]!="(":
            result = 0
            break
        if s[i-1] == "(":
            result += temp

        st.pop()
        temp //= 2
    
    else:
        if not st or st[-1]!="[":
            result = 0
            break
        if s[i-1] == "[":
            result += temp

        st.pop()
        temp //= 3
        
if st:
    print(0)
else:
    print(result)