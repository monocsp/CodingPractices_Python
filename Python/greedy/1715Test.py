receive_count = int(input())
card_count_list = []
result = 0
for i in range(0, receive_count):
    card_count_list.append(int(input()))

##오름차순 정렬
card_count_list.sort()

##카드더미 수 : n
##카드 더미를 작은것부터 a b c d ...라 하면
##(n-1)a + (n-2)b + (n-3)c ...
for index, element in enumerate(card_count_list):
    