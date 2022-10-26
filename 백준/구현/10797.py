num=int(input())
car_num=list(map(int, input().split()))

print(car_num.count(num))


# 풀이 1

# cnt=0
# for i in car_num:
#     if i==num:
#         cnt+=1
        
# print(cnt)