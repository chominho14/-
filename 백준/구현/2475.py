arr = list(map(int, input().split()))
sum_input=0
for i in arr:
    sum_input += i**2

print(sum_input%10)