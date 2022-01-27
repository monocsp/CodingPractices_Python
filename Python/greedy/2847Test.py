level_count = int(input())
level_score_list = []

for i in range(0, level_count):
    level_score_list.append(int(input()))

##점수 최솟점을 기준으로 좌측으로 점수는 감소, 우측으로는 증가
#무한루프 break는 모든 리스트에서 list[n] < list[n+1]일때
result = 0
index = 0
while index != level_count:
    current_score = level_score_list[index]
    #맨 끝에 다다르면 종료
    if index == level_count - 1:
        break
    else:
        #curret_score가 우측보다 크거나 같다면 우측 점수에서 1을 감소한 값을 정한다.
        if current_score >= level_score_list[index+1]:
            level_score_list[index] = level_score_list[index+1] - 1
            result += current_score - (level_score_list[index+1] - 1)
            index = 0
            continue

        #0이 아니라면 좌측도 비교한다.
        if index != 0:
            #current_score가 좌측보다 작거나 같다면
            if current_score <= level_score_list[index-1]:
                level_score_list[index-1] = level_score_list[index] -1
                result += current_score - (level_score_list[index-1] - 1)
                index = 0
                continue
    index += 1

print(result)