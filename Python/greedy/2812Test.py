digit_count, dismiss_count = map(int,input().split())
r_digit = list(input())

#Priority list를 만든다
#만드는방법 list[n] < list[n+1]일때 생성
start_index = 0
priority_list = []
i = 0
while True:

    if len(priority_list) == dismiss_count:
        break

    print(f"current start index : {start_index}")
    if r_digit[i] < r_digit[i+1]:
        temp_list = r_digit[start_index:i+1]
        temp_list.sort()
        start_index = i+2
        priority_list += temp_list
        print(f"current temp_list : {temp_list}")

    if i+1 == len(r_digit) -1:
        temp_list = r_digit[start_index:i + 1]
        temp_list.sort()
        priority_list += temp_list

    i += 1

print(r_digit)
print(priority_list)

if len(priority_list) == 0:
    for i in range(0, dismiss_count):
        r_digit.remove(min(rdigit))
else:
    for i in priority_list:
        r_digit.remove(i)

print(''.join(r_digit))