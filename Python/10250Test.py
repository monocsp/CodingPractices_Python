test_count = int(input())
result_list = []
for i in range(0, test_count):
    receive_input = input().split()
    height = int(receive_input[0])
    width = int(receive_input[1])
    customer = int(receive_input[2])
    room_height = ""
    room_number = ""

    if customer % height == 0:
        room_height = f"{height}"
        room_number = f"{(customer // height)}"
    else:
        room_height = f"{customer % height}"
        room_number = f"{(customer // height) + 1}"

    if int(room_number) < 10:
        room_number = "0" + room_number
    result_list.append(room_height + room_number)

for i in result_list:
    print(i)
