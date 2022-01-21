result = []
while True:
    receive_input = list(map(int, input().split()))
    if sum(receive_input) == 0:
        break
    else:
        l = receive_input[0]
        p = receive_input[1]
        v = receive_input[2]
        t = 0
        if v%p < l:
            t = v%p
        else:
            t = l
        result.append(l*(v//p) + t)

for index, element in enumerate(result):
    print(f"Case {index+1}: {element}")

