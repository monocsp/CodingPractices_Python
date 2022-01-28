class_count = int(input())
class_schedule_list = []
classroom_list = []
for i in range(0, class_count):
    class_schedule_list.append(list(map(int, input().split())))

for index, schedule_list in enumerate(classroom_list):
    