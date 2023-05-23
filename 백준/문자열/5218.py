
a = ["A","B", "C", "D", "E" , "F" , "G" ,"H" , "I","J","K", "L", "M", "N", "O", "P","Q", "R", "S","T","U","V", "W", "X", "Y", "Z"]

t = int(input())

for _ in range(t):
    i_f, i_b = map(str, input().split())
    
    i_f = list(i_f)
    i_b = list(i_b)
    
    print("Distances: ", end="")
    
    for i in range(len(i_f)):
        result = a.index(i_b[i]) - a.index(i_f[i])
        if result < 0:
            result += 26
            
        print(result, end=" ")
    
    print()



