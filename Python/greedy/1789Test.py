receive_int = int(input())
max_number = 0
while True:
    ad = receive_int//3

    for i in range(ad, 0, -1):
        max_number = i
        sum = 0
        for element in range(i, 0, -1):
            sum += element
            if sum > receive_int:
                max_number = 0
                break
        print(f"sum : {sum}")
        if max_number != 0:
            break

    if max_number != 0:
        break

print(max_number)
