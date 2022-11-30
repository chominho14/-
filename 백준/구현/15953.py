t=int(input())

for i in range(t):
    a, b = map(int, input().split())
    price=0
    if a==0:
        price+=0
    elif a==1:
        price+=5000000
    elif a<=3:
        price+=3000000
    elif a<=6:
        price+=2000000
    elif a<=10:
        price+=500000
    elif a<=15:
        price+=300000
    elif a<=21:
        price+=100000
    
    if b==0:
        price+=0
    elif b==1:
        price+=5120000
    elif b<=3:
        price+=2560000
    elif b<=7:
        price+=1280000
    elif b<=15:
        price+=640000
    elif b<=31:
        price+=320000
    print(price)