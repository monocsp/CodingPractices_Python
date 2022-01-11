##-로 split
##+로 split

receive_arithmetic_list = list(input().split('-'))
result = 0
for index, element in enumerate(receive_arithmetic_list):
    temp_list = map(int,element.split('+'))
    receive_arithmetic_list[index] = sum(temp_list)
    if index == 0:
        result = receive_arithmetic_list[0]
    else:
        result -= receive_arithmetic_list[index]

print(result)
