receive_number_list = list(map(int, input()))
if 0 in receive_number_list:
    receive_number_list.remove(0)
    if sum(receive_number_list) % 3 == 0:
        receive_number_list.sort(reverse=True)
        result = ""
        for i in receive_number_list:
            result += str(i)
        print(result+"0")
    else:
        print(-1)
else:
    print(-1)

