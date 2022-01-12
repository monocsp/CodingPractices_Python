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
schedule_dictionary_key_list_desc.sort(reverse=Ture)

for meeting_schedule in schedule_dictionary_key_list_desc:

    
    start = meeting_schedule[0]
    end = meeting_schedule[1]
    save_meeting_schedule = False

    ##방이 이미 존재한다면,
    if room_list:
        ##각 방에 자리가 있는지 확인
        for room in room_list:
            can_this_room = True
            ##각 방의 스케쥴 확인
            for room_schedule in room:
                current_room_schedule_start = room_schedule[0]
                current_room_schedule_end = room_schedule[1]
                if end <= current_room_schedule_start:
                    continue
                elif start >= current_room_schedule_end:
                    continue
                else:
                    can_this_room = False
                    break
            ##현재 방이 가능하다면,
            if can_this_room:
                room.append(meeting_schedule)
                save_meeting_schedule = True

        ##가능한 방이 없을 때
        if not save_meeting_schedule:
            room_list.append(meeting_schedule)

    else:
        room_list

