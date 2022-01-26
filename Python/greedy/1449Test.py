pipe_hole_count, tape_length = map(int,input().split())
hole_list = []

hole_list= list(map(int,input().split()))

hole_list.sort()

#연속한 숫자.
#테이프의 길이에 따라서 숫자의 연속성을 파악.
#end = start -1 + tape_length
tape_count = 0
can_cover_one_tape = False
start_element = 0
end_element = 0
for index, element in enumerate(hole_list):

    if hole_list[index] > end_element:
        tape_count += 1
        start_element = hole_list[index]
        end_element = start_element - 1 + tape_length
    else:
        continue

print(tape_count)