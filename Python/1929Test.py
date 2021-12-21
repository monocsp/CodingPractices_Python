import math
import stopWatch

receive_input = input().split()

prime_number_list = []
mini = int(receive_input[0])
maxi = int(receive_input[1])

stopWatch = stopWatch()
stopWatch.start()
if mini < 3 and maxi > 1:
    prime_number_list.append(2)
for i in range(mini, maxi+1):
    root_i = math.ceil(math.sqrt(i))
    is_prime_number = False
    for j in range(2, root_i + 1):
        if i % j != 0:
            is_prime_number = True
        else:
            is_prime_number = False
            break
    if is_prime_number:
        prime_number_list.append(i)

for i in prime_number_list:
    print(i)
print(len(prime_number_list))
stopWatch.stop()

prime_number_list = []
stopWatch.start()
for i in range(mini, maxi + 1):
    if i == 1:
        continue
    prime_number_list.append(i)

for i in prime_number_list:
    root_i = math.ceil(math.sqrt(i))
    for j in 