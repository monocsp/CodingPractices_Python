import math
test_case = []
result_list = []
while True:
    receive = int(input())
    if receive == 0:
        break
    test_case.append(receive)

for i in test_case:
    count_primary_number = 0
    if i == 1:
        result_list.append(1)
        continue
    else:
        for j in range(i, (2*i+1)):
            if j == 2 or j == 3 or j == 5 or j == 7:
                count_primary_number += 1
                continue
            root_j = int(math.ceil(math.sqrt(j)))
            is_primary_number = True
            for j_root in range(2, root_j):
                if j % j_root == 0:
                    is_primary_number = False
                    break
            if is_primary_number:
                count_primary_number += 1
    result_list.append(count_primary_number)

for i in result_list:
    print(i)



