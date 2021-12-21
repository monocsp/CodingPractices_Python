test_count = int(input())
result_list = []
for i in range(0, test_count):
    pri = [0]
    receive_point = input().split()
    a = int(receive_point[0])
    b = int(receive_point[1])

    height = 0
    for j in range(0, b-a):
        if height != 0:
            if pri[height] == 1 or pri[height] == 2:
                height = 0
                pri[height] += 1
                continue

        if pri[height] < 3:
            pri[height] += 1
        else:
            if pri[height] == 3:
                pri.append(0)
            height += 1
            pri[height] += 1

    result_list.append(pri[0])
    
for i in result_list:
    print(f"{i}")
        