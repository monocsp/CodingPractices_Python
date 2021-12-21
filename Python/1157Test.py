receive_string = input()
#받은 모든 문자를 대문자로 치환
receive_string = receive_string.upper()
#문자 카운트하는 table 변수 선언
hash_table = {}
#가장 많이 입력된 횟수를 저장하는 변수 선언
counter = 0
#가장 많이 입력된 문자를 저장하는 변수 선언
result = ''
#받은 모든 문자를 table에 저장한다.
#table에 이미 저장이 되어있으면 1이 더해지고
#없다면 table에 해당 문자와 1이 함께 저장된다
for i in list(receive_string):
    if i in hash_table:
        hash_table[i] += 1
    else:
        hash_table[i] = 1
#저장된 테이블을 찾는다.
for key in hash_table:
    word_count = hash_table[key]
    #counter가 해당 문자가 작성된 횟수보다 적다면
    #counter가 해당 문자 횟수로 바뀌고
    #해당 문자가 result에 저장된다
    if counter < word_count:
        counter = word_count
        result = key
    #만약 해당 문자가 작성된 횟수가 counter과 동일하다면
    #result는 초기화된다.
    elif counter == word_count:
        result = ''
    #counter가 해당 문자가 작성된 횟수보다 많다면
    #그대로 진행한다.
    else:
        continue
#result 값의 유무에 따라 출력이 달라진다.
if result == '':
    print("?")
else:
    print(result)