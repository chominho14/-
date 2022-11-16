n=int(input())
for _ in range(n):
    p=int(input())
    dic={}
    for _ in range(p):
        price, name=input().split()
        price = int(price)
        dic[price]=name
    print(dic.get(max(dic.keys())))