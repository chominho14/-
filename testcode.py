
a,b1,c=input().split()
w=int(a)
h=int(b1)
b=int(c)

print("{0} MB".format(round(w*h*b/8/1024/1024,2)))