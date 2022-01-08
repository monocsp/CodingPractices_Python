column, row = map(int,input().split())
receive_tile = []
change_count = 0
for i in range(0,column):
    receive_tile.append(input())

for i in range(0, column):
    for j in range(0, row):
        current_tile_color = receive_tile[i][j]
        print(f"current Tile color : {current_tile_color}")
        if j == 0:
            if i != 0:
                under_tile_color = receive_tile[i - 1][j]
                if current_tile_color == under_tile_color:
                    change_list = list(receive_tile[i])
                    if under_tile_color == 'W':
                        change_list[j] = 'B'
                    else:
                        change_list[j] = 'W'
                    receive_tile[i] = "".join(change_list)
                    print(f"1 current Change Tile is : {i, j}")
                    change_count += 1
            else:
                continue
        else:
            left_tile_color = receive_tile[i][j-1]
            if current_tile_color == left_tile_color:
                change_list = list(receive_tile[i])
                if left_tile_color == 'W':
                    change_list[j] = 'B'
                else:
                    change_list[j] = 'W'
                receive_tile[i] = "".join(change_list)
                print(f"2 current Change Tile is : {i,j}")

                change_count += 1

print(change_count)