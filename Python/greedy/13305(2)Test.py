city_count = int(input())
city_to_city_distance = list(map(int,input().split()))
oil_cost = list(map(int,input().split()))

total_cost = 0
sum_distance = 0
current_oil_cost = -1

for index in range(0, city_count-1):
    #현재 기름가격 파악
    #처음 시작경우
    if current_oil_cost < 0:
        current_oil_cost = oil_cost[index]
        sum_distance += city_to_city_distance[index]
    # 오일가격이 기존보다 저렴한 경우
    elif current_oil_cost > oil_cost[index]:
        #도달할때까지의 가격 및 거리 초기화
        total_cost += sum_distance * current_oil_cost
        sum_distance = 0
        #저렴한 가격으로 변경
        current_oil_cost = oil_cost[index]
        sum_distance += city_to_city_distance[index]

    #오일가격이 기존보다 비싼경우
    else:
        sum_distance += city_to_city_distance[index]


if sum_distance != 0:
    total_cost += sum_distance * current_oil_cost

print(total_cost)




