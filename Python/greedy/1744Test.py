receive_length = int(input())
receive_plus_list = []
receive_minus_list = []
is_contain_zero = False
result = 0

for i in range(0, receive_length):
    receive_input = int(input())
    if receive_input > 0:
        receive_plus_list.append(receive_input)
    elif receive_input < 0:
        receive_minus_list.append(receive_input)
    else:
        is_contain_zero = True

receive_plus_list.sort(reverse = True)
receive_minus_list.sort()

#길이가 홀수인지 짝수인지 파악

for index in range(0, len(receive_minus_list)//2):
    result += receive_minus_list[index * 2] * receive_minus_list[(index * 2) + 1]

if len(receive_minus_list) % 2 == 1:
    if not is_contain_zero:
        result += receive_minus_list[-1]

for index in range(0, len(receive_plus_list)//2):
    if receive_plus_list[index * 2] * receive_plus_list[(index * 2) + 1] > receive_plus_list[index * 2] + receive_plus_list[(index * 2) + 1]:
        result += receive_plus_list[index * 2] * receive_plus_list[(index * 2) + 1]
    else:
        result += receive_plus_list[index * 2] + receive_plus_list[(index * 2) + 1]



if len(receive_plus_list) % 2 == 1:
    result += receive_plus_list[-1]

print(result)