
receive_list = [0 for i in range(0,100000001)]
maximum = 0
for i in range(0,int(input())):
    receive_list[int(input())] += 1


for index, element in enumerate(receive_list) :
    for i in range(0, element):
        print(index)


