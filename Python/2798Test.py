card_count, limit = map(int, input().split())
card_list = list(input().split())
maxi = 0

for a in range(0, len(card_list)-2):
    for b in range(a+1, len(card_list)-1):
        for c in range(b+1, len(card_list)):
            total = int(card_list[a]) + int(card_list[b]) + int(card_list[c])
            # print(f"a : {card_list[a]}")
            # print(f"b : {card_list[b]}")
            # print(f"c : {card_list[c]}")
            # print(f"total : {total}")
            # print("--------------------------")
            if total <= limit:
                if total > maxi:
                    maxi = total


print(maxi)