n=list(input())
n_d = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0}

for i in range(len(n)):
    if n[i] in ['6', '9']:
        n_d['6'] += 1
    else:
        n_d[n[i]] += 1
    
if n_d['6'] % 2 == 0:
    n_d['6'] = n_d['6'] // 2
else:
    n_d['6'] = n_d['6'] // 2 + 1

print(max(n_d.values()))