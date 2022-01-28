# 교실 리스트
classroom_list = []

#수업이 겹치는 경우,
#1. 어떤 수업의 시작시간이 다른 수업의 시작과 종료 사이에 있는 경우
#단 수업시작시간이 다른 수업종료시간과 같은경우에는 제외
#2. 어떤 수업의 종료시간이 다른 수업의 시작과 종료사이에 있는 경우
#단 수업종료시간이 다른 수업시작시간과 같은 경우에는 제외


def findClass(schedule):
    current_start = schedule[0]
    current_end = schedule[1]

    for classroom_index, classroom_schedule in enumerate(classroom_list):
        can_save = True

        for classroom_schedule_start_end in classroom_schedule:

            start = classroom_schedule_start_end[0]
            end = classroom_schedule_start_end[1]

            #저장이 되지 않는 경우
            #start <= current_start < end
            if current_start >= start:
                if current_start < end:
                    can_save = False
                    #한번이라도 겹치는 경우가 발생하면 즉시 다음 교실로 탐색하기위해 break
                    break
            # start < current_end <= end
            if current_end > start:
                if current_end <= end:
                    can_save = False
                    break

        #만약 False가 한번도 안 떴다면 그 교실 스케쥴에 저장한다.
        if can_save:
            classroom_list[classroom_index].append(schedule)
            return

    #어떤 교실에도 추가할 수 없다면 새로운 교실을 추가하여 스케쥴을 저장한다.
    if not can_save:
        classroom_list.append([schedule])
        return



if __name__ == "__main__":
    class_count = int(input())
    class_schedule_list = []

    for i in range(0, class_count):
        class_schedule_list.append(list(map(int, input().split())))


    for index, current_class_schedule in enumerate(class_schedule_list):
        #첫 스케쥴인경우 더한다.
        if len(classroom_list) == 0:
            classroom_list.append([current_class_schedule])

        else:

            findClass(current_class_schedule)

    print(len(classroom_list))

