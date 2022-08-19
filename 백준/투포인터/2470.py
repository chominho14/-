import sys
input = sys.stdin.readline

n = int(input())
prov = list(map(int, input().split(' ')))

prov.sort()

start = 0
end = n-1

answer = abs(prov[start]+prov[end])
final = [prov[start],prov[end]]

while start < end:
    left = prov[start]
    right = prov[end]
    
    sum = left + right
    
    if abs(sum) < answer:
        answer = abs(sum)
        final = [left, right]
        if answer == 0:
            break
        
    if sum < 0:
        left += 1
    else:
        right -= 1
        
print(final[0], final[1])