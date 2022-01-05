receive_number = int(input())
receive_digit_number = list(map(int,str(receive_number)))


number = '1'
for a in range(2, len(receive_digit_number)):
    number += '0'

while True:

    number = int(number)
    digit_number = list(map(int,str(number)))
    result = number + sum(digit_number)

    if result == receive_number:
        print(number)
        break

    if number > receive_number:
        print(0)
        break

    number += 1



