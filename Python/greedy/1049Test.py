cut_off_count, brand_count = map(int,input().split())
package_cost = 10000
one_cost = 10000
##가장 저렴한 6개 묶음보다 1개짜리 6개사는게 더 저렴한 경우 True
cheaper_package_cost_than_one_cost = False
for i in range(0, brand_count):
    receive_package_cost, receive_one_cost = map(int, input().split())
    if receive_one_cost < one_cost:
        one_cost = receive_one_cost
    if receive_package_cost < package_cost:
        package_cost = receive_package_cost

if one_cost * 6 < package_cost:
    cheaper_package_cost_than_one_cost = True

if cheaper_package_cost_than_one_cost:
    print(cut_off_count * one_cost)
else:
    if (cut_off_count % 6)*one_cost < package_cost:
        print((cut_off_count//6)*package_cost + (cut_off_count%6)*one_cost)
    else:
        print(((cut_off_count // 6)+1) * package_cost )
