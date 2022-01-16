city_count = int(input())
city_to_city_distance = list(map(int,input().split()))
oil_cost = list(map(int,input().split()))

total_cost = 0


##가장싼곳에서 끝까지
while len(oil_cost) != 0:

    ##가장 싼 오일가격 index
    cheapest_oil_cost_index = oil_cost.index(min(oil_cost))


    ##맨 끝인경우
    if cheapest_oil_cost_index == city_count -1:
        del oil_cost[cheapest_oil_cost_index]

    ##맨 처음인경우
    elif cheapest_oil_cost_index == 0:
        total_distance = sum(city_to_city_distance)
        total_cost += total_distance * oil_cost[cheapest_oil_cost_index]
        oil_cost = []

    else:

        total_distance = 0
        # 가장 싼 지점부터 끝까지 거리의 총합
        for i in range(cheapest_oil_cost_index, len(city_to_city_distance)):
            total_distance += city_to_city_distance[i]

        #가장 싼 지점부터 끝까지 거리까지 금액
        total_cost += oil_cost[cheapest_oil_cost_index] * total_distance

        #가장싼 지점부터 끝까지 삭제
        del city_to_city_distance[cheapest_oil_cost_index: len(city_to_city_distance)]
        del oil_cost[cheapest_oil_cost_index: len(oil_cost)]



print(total_cost)


