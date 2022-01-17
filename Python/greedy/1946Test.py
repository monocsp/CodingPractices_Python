receive_test_count = int(input())

def hiring(count):
    grade = []
    drop_count = 0
    #grade받아오기
    for i in range(0, count):
        grade.append(list(map(int, input().split())))
    #서류기준으로 탈락자
    grade.sort(key=lambda x:x[0])
    base_interview_grade = grade[0][1]
    for index, i in enumerate(grade):
        current_interview_grade = i[1]
        if current_interview_grade > base_interview_grade:
            drop_count += 1

    # 면접기준으로 탈락자
    grade.sort(key=lambda x:x[1])
    base_document_grade = grade[0][0]
    for index, i in enumerate(grade):
        current_document_grade = i[0]
        if current_document_grade > base_document_grade:
            drop_count += 1



    return (count - drop_count)


for i in range(0,receive_test_count):
    apply_count = int(input())
    print(hiring(apply_count))