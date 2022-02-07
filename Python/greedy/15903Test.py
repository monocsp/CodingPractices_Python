card_count, merge_count = map(int,input().split())
card_list = list(map(int,input().split()))

for i in range(0, merge_count):
    #리스트 최솟값 추출
    x = min(card_list)
    card_list.remove(x)
    # 리스트 두번째 최솟값 추출
    y = min(card_list)
    card_list.remove(y)


    merge_result = x + y

    card_list.append(merge_result)
    card_list.append(merge_result)

print(sum(card_list))
