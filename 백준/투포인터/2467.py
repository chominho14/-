N = int(input())
prov = list(map(int, input().split()))

start = 0
end = N-1

standard = abs(prov[start] + prov[end])
result = [prov[start], prov[end]]

while start < end:
    left = prov[start]
    right = prov[end]
    sum = left + right
    
    if abs(sum) < standard:
        standard = abs(sum)
        result = [left, right]
        if standard == 0:
            break
    if sum < 0:
        start += 1
    else:
        end -= 1

print(result[0], result[1])