row, column = map(int,input().split())
pip_map = []
result = 0
for i in range(0, column):
    pip_map.append(list(input()))

for index_row in range(0, row):
    #오른쪽으로 간 횟수
    right = 0
    before_pip_map = pip_map
    for index_column in range(0, column):
        current_row = index_row + right

        # print(f"current {pip_map[index_column][current_row]}")
        # for i in pip_map:
        #     print(i)
        # print("------------------------------------")

        #만약 시작지점에 X(건물)이 존재한다면 파이프를 놓지못하므로 넘어간다.
        if index_column == 0:
            # if pip_map[index_column][index_row] == 'X':
            if pip_map[index_column][index_row] == 'X':
                break


        #마지막번째 열까지 도착했다면
        if index_column + 1 == column:
            pip_map[index_column][current_row] = 'X'
            result += 1
            break

        #바로 아래에 건물이 없다면 현재 위치에 파이프를 놓고 X표시를 한다.
        if pip_map[index_column+1][current_row] == '.':
            pip_map[index_column][current_row] = 'X'
            continue
        # 바로 아래에 건물이 있다면 오른쪽아래 대각선을 살펴본다.
        else:
            #오른쪽 밖을 벗어나지 않는 경우
            if current_row + 1 < row:

                #오른쪽 아래 대각선에 건물이 없다면,
                if pip_map[index_column+1][current_row+1] == '.':
                    right += 1
                    pip_map[index_column][current_row] = 'X'
                    continue

                #오른쪽아래 대각선에 건물이 존재한다면.
                else:
                    pip_map = before_pip_map
                    break
            #오른쪽을 벗어나는 경우.
            else:
                pip_map = before_pip_map
                break

print(result)
