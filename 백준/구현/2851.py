score=[]
for _ in range(10):
    score.append(int(input()))
    
cnt=0
result=[]
cal=[]
for i in score:
    cnt+=i
    result.append(cnt)
    cal.append(abs(100-cnt))
    
if cal.count(min(cal))>0:
    print(result[cal.index(min(cal)) + cal.count(min(cal)) - 1])
else:
    print(result[cal.index(min(cal))])
