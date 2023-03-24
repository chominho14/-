num = []

sum_num = 0

for _ in range(5):
    t = int(input())
    sum_num += t
    num.append(t)

# num 정렬
num.sort()

avg_num = sum_num//5

print(avg_num)
print(num[2])


