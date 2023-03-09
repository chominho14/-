t = int(input())

# 3 <= k <= 1000 이므로 최대 n이 46보다 작아야 한다. (여유가 있으므로 임의로 49로 지정)
tn = []
for i in range(1,49):
    tn.append(i*(i+1)/2)
    
# for 문 3개를 돌려 모든 경우의 수를 찾는다.
def check(k):
    flag = False
    for i in range(0, 48):
        for j in range(i, 48):
            for p in range(j, 48):
                if tn[i] + tn[j] + tn[p] == k:
                    flag = True
    return flag

for _ in range(t):
    k = int(input())
    
    if check(k):
        print(1)
    else:
        print(0)
