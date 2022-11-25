coordinate_x=[]
coordinate_y=[]

for _ in range(3):
    x, y = map(int, input().split())
    coordinate_x.append(x)
    coordinate_y.append(y)

for i in range(3):
    if coordinate_x.count(coordinate_x[i])==1:
        x=coordinate_x[i]
    if coordinate_y.count(coordinate_y[i])==1:
        y=coordinate_y[i]
    
print(x, y)