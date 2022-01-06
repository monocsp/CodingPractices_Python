card_count, limit = map(int, input().split())
card_list = list(input().split())
maxi = 0

#a는 첫번째 카드, b는 두번째 카드, c는 세번째 카드이다.
#첫번째 카드는 가장 우측에 도달했을 때에는 두 카드도 우측에 도착한 상태이므로 -2를 해준다.
for a in range(0, len(card_list)-2):
    # 두번째 카드가 시작할 때에는 첫번째 카드가 좌측에 있으므로 +1를 해준다.
    # 두번째 카드는 가장 우측에 도달했을 때에는 한장의 카드만 우측에 도착한 상태이므로 -1를 해준다.
    for b in range(a+1, len(card_list)-1):
        # 세번째 카드가 시작할 때에는 첫번째,두번째 카드가 좌측에 있으므로 +2를 해준다.
        # 세번째 카드는 가장 우측에 도달했을 때에는 가장 우측에있으므로 그대로 둔다.
        for c in range(b+1, len(card_list)):
            total = int(card_list[a]) + int(card_list[b]) + int(card_list[c])
            if total <= limit:
                if total > maxi:
                    maxi = total

print(maxi)