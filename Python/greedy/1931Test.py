receive_schedule_count = int(input())
schedule_dictionary = {}
room_list = []


for i in range(0, receive_schedule_count):
    receive_start, receive_end = map(int, input().split())
    work_time = receive_end - receive_start
    if work_time in schedule_dictionary:
        schedule_dictionary[work_time].append([receive_start, receive_end])
    else:
        schedule_dictionary[work_time] = [[receive_start, receive_end]]

schedule_dictionary_key_list_desc = list(schedule_dictionary.keys())
schedule_dictionary_key_list_desc.sort(reverse=True)

#같은 회의시간
for desc_time in schedule_dictionary_key_list_desc:

    for meeting_schedule in schedule_dictionary[desc_time]:
        start = meeting_schedule[0]
        end = meeting_schedule[1]
        save_meeting_schedule = False

        ##방이 이미 존재한다면,
        if room_list:
            ##각 방에 자리가 있는지 확인
            for room in room_list:
                can_this_room = False

                ##각 방의 스케쥴 확인
                if start in room:
                    continue
                else:
                    for key_start, value_end in room.items():
                        if end <= key_start or start >= value_end:
                            can_this_room = True


                ##현재 방이 가능하다면,
                if can_this_room:
                    room[start] = end
                    save_meeting_schedule = True

            ##가능한 방이 없을 때
            if not save_meeting_schedule:
                room_list.append({start:end})

        ##방이 처음이라면,
        else:
            room_list.append({start:end})

print(len(room_list))