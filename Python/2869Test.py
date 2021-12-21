receive_input = input().split()
snail_climb = int(receive_input[0])
snail_fall = int(receive_input[1])
stick_height = int(receive_input[2])


#우변이 소수점이 발생하는 지 체크한다.
if (stick_height - snail_fall) % (snail_climb - snail_fall) == 0:
    #자연수로 떨어진다면, 하루에 갈 수 있는 거리 딱 맞게 나무 막대 정상에 도착한다는 뜻이다.
    print((stick_height - snail_fall)//(snail_climb - snail_fall))
    # 소수점이 발생하면, 하루에 갈 수 있는 거리 중간에 나무 막대 정상에 도착한다는 뜻이다.
else:
    print(((stick_height - snail_fall)//(snail_climb - snail_fall))+1)