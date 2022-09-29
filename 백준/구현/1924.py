x, y=map(int, input().split())

month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

before_month_day = 0
for i in range(x):
    before_month_day += month[i]
    
result_day = before_month_day + y
k = result_day%7
week = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
print(week[k])