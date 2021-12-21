receive_input = input().split()
immutable_coast = int(receive_input[0])
mutable_coast = int(receive_input[1])
price = int(receive_input[2])
break_even_point = 0
if mutable_coast < price :
    break_even_point = (immutable_coast//(price - mutable_coast))+1
    print(break_even_point)
else:
    print(-1)