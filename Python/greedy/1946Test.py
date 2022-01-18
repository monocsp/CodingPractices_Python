receive_test_count = int(input())



def hiring(count):
    grade = []
    drop_count = 0

    first_document_grade = []
    first_interview_grade = []
    #grade받아오기
    before_grade = []
    for i in range(0, count):
        before_grade
        document_grade, interview_grade = map(int, input().split())

        if document_grade == 1:
            first_document_grade.append(document_grade)
            first_document_grade.append( interview_grade)
        if interview_grade == 1:
            first_interview_grade.append(document_grade)
            first_interview_grade.append(interview_grade)

        # if len(first_document_grade) == 2:
        #     if interview_grade > first_interview_grade[1]:
        #         continue
        #
        # if len(first_interview_grade) == 2:
        #     if document_grade > first_document_grade[0]:
        #         continue

        grade.append([document_grade, interview_grade])

    for i in grade:
        current_document_grade = i[0]
        current_interview_grade = i[1]

        #서류기준으로 탈락자
        #면접순위로 비교
        if current_interview_grade > first_document_grade[1]:
            drop_count += 1
        # 면접기준으로 탈락자
        # 서류순위로 비교
        elif current_document_grade > first_interview_grade[0]:
            drop_count += 1


    return (count - drop_count)


for i in range(0,receive_test_count):
    apply_count = int(input())
    print(hiring(apply_count))