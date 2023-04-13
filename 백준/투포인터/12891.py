s, p = map(int, input().split())
dna = input()
acgt = ['A', 'C', 'G', 'T']
min_acgt = list(map(int, input().split()))
cnt = 0

left = 0
right = p-1

dna_slice = dna[:p]
cnt_acgt = [0, 0, 0, 0]

flag = True

for i in range(4):
    cnt_acgt[i] = dna_slice.count(acgt[i])
 

for i in range(4):
    if min_acgt[i] > cnt_acgt[i]:
        flag = False
        
if flag:
   cnt+=1 


for i in range(1, s - p + 1):
    left += 1
    right += 1
    flag = True
    for j in range(4):
        if dna[left-1] == acgt[j]:
            cnt_acgt[j] -= 1
    
    for j in range(4):
        if dna[right] == acgt[j]:
            cnt_acgt[j] += 1
  
    for j in range(4):
        if min_acgt[j] > cnt_acgt[j]:
            flag = False
        
    if flag:
        cnt+=1 
    
    
print(cnt)
