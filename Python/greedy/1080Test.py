receive_weight_count = int(input())
weight_list = []

weight_list = list(map(int,input().split()))
##추의 무게 순차적으로 정렬
weight_list.sort()

##연속되지않은숫자가 발견되는경우
##총합 + 1과 다음숫자 비교
sum = 0
for index,element in enumerate(weight_list):
    ##만약 첫번째 추가 1이 아니라면 반드시 1이 가장 작은 무게
    if index == 0:
        if element != 1:
            break
    sum += element

    if index == len(weight_list)-1:
        break

    next_element = weight_list[index + 1]
    if element + 1 != next_element:
        if sum+1 < next_element:
            break

print(f"{sum + 1}")