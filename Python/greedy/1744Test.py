#숫자의 총 길이
receive_length = int(input())
#양수리스트
receive_plus_list = []
#음수리스트
receive_minus_list = []
#0이 존재하는지 확인
is_contain_zero = False
result = 0

for i in range(0, receive_length):
    receive_input = int(input())
    #받은 값이 양수라면 양수리스트에 추가
    if receive_input > 0:
        receive_plus_list.append(receive_input)
    # 받은 값이 음수라면 음수리스트에 추가
    elif receive_input < 0:
        receive_minus_list.append(receive_input)
    #받은 값이 0이라면 True
    else:
        is_contain_zero = True
#절댓값이 가장 큰 숫자부터 묶기때문에 양수리스트는 내림차순으로 정렬.
receive_plus_list.sort(reverse = True)
receive_minus_list.sort()

#음수리스트에서 2개씩 묶어서 result에 더해준다.
for index in range(0, len(receive_minus_list)//2):
    result += receive_minus_list[index * 2] * receive_minus_list[(index * 2) + 1]

#음수리스트 길이가 홀수이면 두개씩 묶고 한개가 남으므로 더해주어야 한다.
#0이 존재하면 묶어서 0으로 처리가능하지만, 0이 없다면 어쩔수없이 빼주어야 한다.
if len(receive_minus_list) % 2 == 1:
    #0이 없다면 마지막 음수를 빼준다.
    if not is_contain_zero:
        #list[-1]은 마지막번째를 불러온다.
        result += receive_minus_list[-1]

#양수리스트 또한 더해준다. 다만, 양수리스트는 (1*1)보다 1+1이 더 큰 예외적인 경우가 발생한다.
#따라서 list[n]+list[n+1]과 list[n]*list[n+1] 중, 더 큰 것을 더해준다.
for index in range(0, len(receive_plus_list)//2):
    if receive_plus_list[index * 2] * receive_plus_list[(index * 2) + 1] > receive_plus_list[index * 2] + receive_plus_list[(index * 2) + 1]:
        result += receive_plus_list[index * 2] * receive_plus_list[(index * 2) + 1]
    else:
        result += receive_plus_list[index * 2] + receive_plus_list[(index * 2) + 1]

#양수리스트가 홀수라면 마지막 리스트를 더해준다.
if len(receive_plus_list) % 2 == 1:
    result += receive_plus_list[-1]

print(result)