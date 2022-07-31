T = int(input())

for i in range(T):
    N, M = map(int,input().split())
    imp = list(map(int, input().split()))
    opt = list(range(len(imp)))
    opt[M] = "target"
    cnt=0
    
    while True:
        if imp[0] == max(imp): 
            cnt+=1

            if opt[0] == "target":
                print(cnt)
                break
            else:
                imp.pop(0)
                opt.pop(0)
            
        else:
            imp.append(imp.pop(0))
            opt.append(opt.pop(0))
