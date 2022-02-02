multi_tap_count, total_use_count = map(int,input().split())
use_list = list(map(int,input().split()))

result = 0
multi_tap = []

for index, element in enumerate(use_list):
    print(f"current element : {element}")
    if len(multi_tap) < multi_tap_count:
        multi_tap.append(element)
    elif len(multi_tap) == multi_tap_count:
        #만약 동일한것이 존재하지 않는다면,
        if element not in multi_tap:
            #멀티탭에 꽂혀있는 것에서 weight를 비교한다.
            #[weight_number, weight]로 저장
            schedule_number = []
            for ele in multi_tap:
                #첫 비교
                if len(schedule_number) == 0:
                    schedule_number = [ele, use_list.count(ele)]
                else:
                    #그 이후
                    print(f"use list.count(ele) : {use_list.count(ele)},")
                    if use_list.count(ele) < schedule_number[1]:
                        schedule_number = [ele, use_list.count(ele)]
            print(schedule_number)

            multi_tap[multi_tap.index(schedule_number[0])] = element
            result += 1

    print(f"multi_tap : {multi_tap}")
    print(f"use_list : {use_list}")

print(result)