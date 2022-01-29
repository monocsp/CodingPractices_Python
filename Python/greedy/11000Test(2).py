def createList(schedule):
    print(schedule)
    createlist = [True for i in range(200000)]
    for i in range(schedule[0],schedule[1]):
        createlist[i] = False
    return createlist


if __name__ == "__main__":
    class_count = int(input())
    class_schedule_list = []
    classroom_list = []
    for i in range(0, class_count):
        class_schedule_list.append(list(map(int, input().split())))

    #받아온 데이터값을 for구문 돌린다
    for receive_schedule in class_schedule_list:
        if len(classroom_list) == 0:
            classroom_list.append(createList(receive_schedule))
        else:
            for index, schedule_list in enumerate(classroom_list):
                for classroom_schedule_list in classroom_list:
                    can_save = True
                    for element in range(receive_schedule[0], receive_schedule[1]):
                        if not classroom_schedule_list[element]:
                            can_save = False
                            break

                        if can_save:
                            classroom_schedule_list[element][receive_schedule[0]: receive_schedule[1]] = False
                            break
                    if not can_save:
                        classroom_list.append(createList(receive_schedule))
                    else:
                        break
        print(classroom_list)
print(len(classroom_list))