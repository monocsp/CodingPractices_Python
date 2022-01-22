start, end = map(int, input().split())
change_count = 0
while True:
    remainder = end % 2
    if remainder == 1:
        if str(end)[-1] != '1':
            print(str(end)[-1])
            break
        else:
            end = (end - 1) // 10
            change_count += 1
    else:
        end = end // 2
        change_count += 1

    if start == end:
        print(change_count)
        break

    print(f"end : {end+1}")
    print(f"change count : {change_count}")
