digit_count, dismiss_count = map(int,input().split())
r_digit = list(input())

#Priority list를 만든다
#만드는방법 list[n] < list[n+1]일때 생성
start_index = 0
priority_list = []
while True:
    i = 0
    if r_digit[i] < r_digit[i+1]:
        temp_list = r_digit[start_index:i+1]
        temp_list.sort()
        start_index = i+1
        priority_list.append( temp_list)

    if i+1 == len(r_digit) -1:
        break

    if len(priority_list) == dismiss_count:
        break

if len(priority_list) == 0:
    for i in range(0, dismiss_count):
        r_digit.remove(min(rdigit))
else:
    for i in priority_list:
        r_digit.remove(i)

print(''.join(r_digit))