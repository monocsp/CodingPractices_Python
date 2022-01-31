#전체 길이가 홀짝판별
#짝수 -> 모든 문자의 갯수가 짝수
#홀수 -> 하나의 문자는 홀수개이어야하고 나머진 모두 짝수개
receive_word = input()
#받은 문자열을 정렬
receive_word = ''.join(sorted(receive_word))
#문자열이 홀수라면 True, 짝수라면 False
is_odd = len(receive_word) % 2 == 1
#데칼코마니처럼 찍어내기 위해서 홀수인 문자열을 저장하기 위한 변수
odd_word = ''
#팰린드롬이 가능하다면 True, 불가능하다면 False
can_pall = True


#문자열 정리
word_dic = {}
before_word = ''

for i in range(0, len(receive_word)):
    #현재 단어가 이전단어와 다른경우
    if before_word != receive_word[i]:
        if before_word != '':
            #이전단어의 갯수가 홀수인지 짝수인지 확인한다
            #홀수라면,
            if word_dic[before_word] % 2 == 1:
                if is_odd:
                    # 홀수갯수의 문자가 처음이라면 False로 바꾼다.
                    # 홀수문자를 저장한다.
                    is_odd = False
                    odd_word = before_word
                else:
                    #문자열이 짝수일때, 홀수갯수의 문자가 존재하거나,
                    #문자열이 홀수일때, 홀수갯수의 문자가 두 개 이상일때
                    can_pall = False
                    break
        #이전단어를 저장한다.
        before_word = receive_word[i]
        #현재 단어를 dictionary에 추가한다.
        word_dic[receive_word[i]] = 1

    #이전 단어가 현재 단어와 같다면 갯수 1을 추가해준다.
    else:
        word_dic[receive_word[i]] += 1

#만약 is_odd가 안변하면 마지막단어가 홀수
if (len(receive_word) % 2 == 1) == is_odd == True:
    odd_word = receive_word[-1]

#결과값 생성
result = ''
for key in word_dic.keys():
    result += key * (word_dic[key] // 2)

#팰린드롬 문자열을 만들 수 있는지 확인하고 출력한다.
if can_pall:
    if odd_word == '':
        #데칼코마니처럼 result를 출력 후 반대로 출력
        #짝수인 경우, 반대로만 출력
        print(result+result[::-1])
    else:
        #홀수인 경우, 홀수인 문자 하나만 가운데에 두고 반대로 출력
        print(result+odd_word+result[::-1])
else:
    print("I'm Sorry Hansoo")

