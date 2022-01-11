coin_count, limit = map(int,input().split())
coin_list = []
minimum_coin_count = 0

for i in range(0, coin_count):
    coin_list.append(int(input()))

for coin in coin_list[::-1]:
    if limit >= coin:
        minimum_coin_count += limit // coin
        limit -= coin*(limit // coin)

print(minimum_coin_count)
