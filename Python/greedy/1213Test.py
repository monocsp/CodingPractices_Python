#전체 길이가 홀짝판별
#짝수 -> 모든 문자의 갯수가 짝수
#홀수 -> 하나의 문자는 홀수개이어야하고 나머진 모두 짝수개
receive_word = input()
receive_word = ''.join(sorted(receive_word))
is_odd = len(receive_word) % 2 == 1
odd_word = ''
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
                #홀수갯수의 문자가 처음이라면 False로 바꾼다.
                if is_odd:

                    is_odd = False
                    odd_word = before_word
                else:
                    can_pall = False
                    break
        before_word = receive_word[i]
        word_dic[receive_word[i]] = 1
    #같다면
    else:
        word_dic[receive_word[i]] += 1

#만약 is_odd가 안변하면 마지막단어가 홀수
if (len(receive_word) % 2 == 1) == is_odd == True:
    odd_word = receive_word[-1]

#결과값 생성
result = ''
for key in word_dic.keys():
    result += key * (word_dic[key] // 2)

if can_pall:
    if odd_word == '':
        print(result+result[::-1])
    else:
        print(result+odd_word+result[::-1])
else:
    print("I'm Sorry Hansoo")

