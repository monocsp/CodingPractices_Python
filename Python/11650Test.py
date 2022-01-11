receive_count = int(input())
coordinate = {}
for i in range(0, receive_count):
    x,y = map(int,input().split())
    if x in coordinate:
        coordinate[x].append(y)
    else:
        coordinate[x] = [y]
x_list = list(coordinate.keys())
x_list.sort()
for x in x_list:
    y_list = coordinate[x]
    y_list.sort()
    for y in y_list:
        print(f"{x} {y}")

