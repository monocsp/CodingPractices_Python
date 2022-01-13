receive_number_list = map(int,input())
if 0 in receive_number_list:
    receive_number_list.remove(0)
    
else:
    print(-1)