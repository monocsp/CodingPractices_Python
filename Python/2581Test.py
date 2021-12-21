import math

mini = int(input())
maxi = int(input())
list_num = []

for i in range(mini , maxi+1):
    save = True
    # root_aq = math.ceil(math.sqrt(i))
    for j in range(2, i):
        if i % j == 0:
            save = False
            break
    if save and i != 1:
        list_num.append(i)
if len(list_num) == 0:
    print("-1")
else:
    print(sum(list_num))
    print(list_num[0])

