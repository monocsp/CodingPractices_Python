##결과가 저장될 리스트
result = []
while True:
    receive_input = list(map(int, input().split()))

    ##모두 0이라면 종료
    if sum(receive_input) == 0:
        break
    else:
        l = receive_input[0]
        p = receive_input[1]
        v = receive_input[2]

        ##t는 v%p와 l의 관계에 따라 바뀐다.
        t = 0
        ##v%p가 l보다 작은경우, v%p만큼 추가적으로 캠핑을 즐긴다.
        if v%p < l:
            t = v%p
        ##v%p가 l보다 큰경우, l만큼 추가적으로 캠핑을 즐긴다.
        else:
            t = l
        ##결과 저장
        result.append(l*(v//p) + t)

for index, element in enumerate(result):
    print(f"Case {index+1}: {element}")

