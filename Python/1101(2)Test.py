import math

test_count = int(input())
result_list = []
for i in range(0, test_count):
    receive_input = input().split()
    a = int(receive_input[0])
    b = int(receive_input[1])
    distance = b-a
    n = math.ceil(math.sqrt(distance))

    if distance > n * (n-1):
        result_list.append(2*n-1)
    else:
        result_list.append(2*(n-1))
for i in result_list:
    print(i)
