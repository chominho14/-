# 추후에 다시 풀어보기

c = input()
st = []
temp = {"H":1, "C":12, "O":16}

for i in range(len(c)):
    
    if c[i] == "(":   
        st.append(c[i])
        
    elif c[i] == ")":
        check = 0
        
        while True:
            target = st.pop()
            
            if target == "(":
                break
            
            check += target
        
        st.append(check)
              
    elif c[i] in temp:
        st.append(temp[c[i]])
     
    else:
        st[-1] *= int(c[i])

print(sum(st))



# c = input()
# st_l = []
# st = [0]
# b = []

# for i in range(len(c)):
    
#     if c[i] == "(":
#         st_l.append(c[i])
#         if b:
#             st.append(sum(b))
#             b = []
            
        
#     elif c[i] == ")":
#         st_l.pop()
#         if b:
#             st.append(sum(b))
            
#             b = []
    
#     else:
       
#         if c[i] == "H":
#             b.append(1)
#         elif c[i] == "C":
#             b.append(12)
#         elif c[i] == "O":
#             b.append(16)
#         else:
#             if c[i-1] == ")":
#                 st[-1] = int(c[i]) * st.pop()
#             else:
#                 b[-1] *= int(c[i])
    
    

# print(sum(st))
    