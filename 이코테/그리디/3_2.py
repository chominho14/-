
N, M, K = map(int, input().split())
prov = list(map(int, input().split()))
result = 0
prov.sort()

# if prov.count(max(prov)) > 1:
#     result = max(prov) * M
# else:
#     result = (K*max(prov) * (M//K)) + (prov[-2] * (M % K)) 
result = (K*max(prov) * (M//K)) + (prov[-2] * (M % K)) 
    
print(result)