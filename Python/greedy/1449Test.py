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

    if not can_cover_one_tape:
        start_element = hole_list[index]
        end_element = start_element - 1 + tape_length
    if hole_list[index] > end_element:
        continue
    else:
        continue
# while len(hole_list) != 0:
#     start_element = hole_list[0]
#     end_element = start_element - 1 + tape_length
#     end_index = 1
#     for index, element in enumerate(hole_list):
#         #0은 시작지점
#         if index == 0:
#             continue
#         if index == len(hole_list)-1:
#             hole_list = []
#         #테이프길이가 닿는 최대거리를 벗어나는 곳에 구멍이 있다면, 그 전까지 덮는다.
#         if hole_list[index] > end_element:
#             end_index = index
#             break
#     #덮어진 구멍은 삭제.
#     print(f"end index : {end_index}")
#     del hole_list[0:end_index]
#     print(hole_list)
#     tape_count += 1

print(tape_count)