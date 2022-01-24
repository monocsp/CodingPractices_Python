cut_off_count, brand_count = map(int,input().split())
package_cost = 10000
one_cost = 10000
##가장 저렴한 6개 묶음보다 1개짜리 6개사는게 더 저렴한 경우 True
cheaper_package_cost_than_one_cost = False
for i in range(0, brand_count):
    receive_package_cost, receive_one_cost = map(int, input().split())

    ##가장 작은 가격인지 확인
    if receive_one_cost < one_cost:
        one_cost = receive_one_cost
    ##가장 작은 가격인지 확인
    if receive_package_cost < package_cost:
        package_cost = receive_package_cost
##가장 저렴한 6개 묶음보다 1개짜리 6개사는게 더 저렴한 경우 True
if one_cost * 6 < package_cost:
    cheaper_package_cost_than_one_cost = True
##1개짜리로 모두 사는게 싼 경우
if cheaper_package_cost_than_one_cost:
    print(cut_off_count * one_cost)
else:
    ##패키지로 사고 남은것 중 패키지로사는것과 한개짜리로 사는경우 비교
    if (cut_off_count % 6)*one_cost < package_cost:
        print((cut_off_count//6)*package_cost + (cut_off_count%6)*one_cost)
    else:
        print(((cut_off_count // 6)+1) * package_cost )
