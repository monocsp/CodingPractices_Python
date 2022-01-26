receive_word = list(map(str,input()))
check_word = list(map(str,input()))

result = 0
while True:

    if len(receive_word) == 0 or len(receive_word) < len(check_word):
        break

    #첫번째 문자 비교
    first_word = receive_word[0]
    if first_word != check_word[0]:
        #같지않으면 제거.
        receive_word = receive_word[1:]
        continue

    is_same_word = True
    for index, element in enumerate(check_word):
        if element != receive_word[index]:
            is_same_word = False
            receive_word = receive_word[index:]
            break

    if is_same_word:
        receive_word = receive_word[len(check_word):]
        result += 1

print(result)
