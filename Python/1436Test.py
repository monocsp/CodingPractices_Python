receive_input = int(input())
number = 666
count = 0

while True:
    is_continuous = False
    list_digit = list(map(int, str(number)))
    six_index = -1
    index_count = 0
    pre_element = -1
    try:
        list_six_index = [i for i, e in enumerate(list_digit) if e == 6]
        if len(list_six_index) > 2:
            six_index = -1
            index_count = 0
            pre_element = -1

            for index, element in enumerate(list_six_index):
                six_index = index
                if index_count == 0:
                    index_count += 1

                else:
                    if element == pre_element + 1:
                        index_count += 1
                    else:
                        index_count = 1

                pre_element = element

        if index_count > 2:
            is_continuous = True

    except ValueError as valueError:
        continue

    if is_continuous:
        count += 1
        print(f"count : {count} , number : {number}")

    if count == receive_input:
        break

    number += 1

print(number)


# list_digit = list(map(int, str(66000066)))
#
# list_six_index = [i for i, e in enumerate(list_digit) if e == 6]
# print(list_six_index)
# if len(list_six_index) > 2:
#     six_index = -1
#     index_count = 0
#     pre_element = -1
#
#     for index, element in enumerate(list_six_index):
#         six_index = index
#         if index_count == 0:
#             index_count += 1
#
#         else:
#             if element == pre_element + 1:
#                 index_count += 1
#             else:
#                 index_count = 1
#
#         pre_element = element
#
# print(index_count)