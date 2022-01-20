receive_count = int(input())
card_count_list = []
result = 0
for i in range(0, receive_count):
    card_count_list.append(int(input()))


while len(card_count_list) != 1:
    sum = 0
    ##가장작은 두 수 가져오고 삭제
    for i in range(0,2):
        min_index = card_count_list.index(min(card_count_list))
        sum += card_count_list[min_index]
        del card_count_list[min_index]

    result += sum
    card_count_list.append(sum)




print(result)