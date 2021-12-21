def i_can_over_mean():
    #테스트하는 숫자를 받는다.
    test_count = int(input())
    #테스트 결괏값을 저장하는 리스트이다.
    result_arr = []
    #테스트 횟수를 range를 통해 반복한다.
    for i in range(0,test_count):
        #스페이스바로 나누어져 있는 입력값을 리스트 형태로 받는다.
        receive_input_arr = input().split()
        #테스트마다 평균값을 받아야 하는 변수 선언
        current_mean = 0
        #각 테스트마다 점수를 몇개 입력하는 지 저장하는 변수 선언
        current_receive_score_count = int(receive_input_arr[0])
        #맨 앞의 리스트 삭제하여 코드를 좀 더 깔끔하게 다듬을 수 있게 한다.
        del receive_input_arr[0]
        #점수 리스트에서 평균을 구한다.
        for j in receive_input_arr:
            current_mean += int(j)
        current_mean = current_mean/current_receive_score_count
        #평균보다 넘는 점수를 카운팅하는 변수 선언
        mean_over_count = 0
        #점수 리스트에서 평균 넘는 점수를 비교하여 카운팅한다.
        for j in receive_input_arr:
            if current_mean < int(j):
                mean_over_count += 1
        #카운팅한 것을 백분위로 나타내어 결괏값을 저장한다.
        result_arr.append(format(mean_over_count/current_receive_score_count*100,".3f"))
    #결괏값 출력
    for i in result_arr:
        print(f"{i}%")

if __name__ == "__main__":
    i_can_over_mean()