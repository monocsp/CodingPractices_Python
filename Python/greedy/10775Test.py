#1~G1게이트까지 비행기가 착륙할 수 있다.
#최대한 G1게이트부터 채우는 것이 우선이다.
gate_count = int(input())
plain_count = int(input())
#도킹한 게이트
dock_gate_dic = {}
#도킹을 계속할 수 있는지 여부 확인.
# can_docking = True
#
# for i in range(0, plain_count):
#     can_dock_gate_number = int(input())
#     #받아온 게이트 가장 큰 번호부터 -1 감소하며 찾는다.
#     if can_docking:
#         for gate_number in range(can_dock_gate_number, 0, -1):
#             #만약 도킹한 게이트번호가 존재한다면,
#             if gate_number in dock_gate_dic:
#                 #1번 게이트번호까지 존재한다면 도킹을 하지 못하므로 False로 변경
#                 if gate_number == 1:
#                     can_docking = False
#                 #만약 아니라면 계속해서 찾는다.
#                 else:
#                     continue
#             #만약 도킹한 게이트번호가 존재하지 않는다면, 저장하고 반복문 종료
#             else:
#                 dock_gate_dic[gate_number] = True
#                 break
#
# #도킹한 게이트 수 길이를 출력.
# print(len(dock_gate_dic.keys()))
#
can_docking_number = []

for i in range(0, plain_count):
    can_docking_number.append(int(input()))

for can_gate_maxi_number in can_docking_number:
    for gate_number in range(can_gate_maxi_number, 0, -1):
        if gate_number in dock_gate_dic:
            if gate_number == 1:
                print(len(dock_gate_dic.keys()))
                quit()
        else:
            dock_gate_dic[gate_number] = True
            break

print(plain_count)
