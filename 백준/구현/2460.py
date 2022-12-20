result = 0
num = 0

for _ in range(10):
    p_in, p_out = map(int, input().split())
    
    num -= p_in
    num += p_out
    
    result = max(num, result)
    
print(result)