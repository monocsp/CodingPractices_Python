size_list = []
receive_count = int(input())
for i in range(0, receive_count):
    weight, height = map(int, input().split())
    size_list.append([weight, height])

sort_height