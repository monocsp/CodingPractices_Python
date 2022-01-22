start, end = map(int, input().split())
change_count = 0

while True:
    ##2로 나누어 떨어지는지 확인
    remainder = end % 2

    ##2로 나누었을 때, 나머지가 1인 경우
    if remainder == 1:
        ##끝자리가 1인지 확인
        ##끝자리가 1이 아니라면 -1출력
        if str(end)[-1] != '1':
            print('-1')
            break
        ##끝자리가 1이 이라면 N*10 +1을 반대로 변환
        else:
            end = (end - 1) // 10
            change_count += 1

    ##2로 나누었을 때, 나머지가 0인 경우
    else:
        ##2로 나눔
        end = end // 2
        change_count += 1


    if start == end:
        print(change_count+1)
        break
    ##start보다 작아지는 경우.
    elif start > end:
        print('-1')
        break


