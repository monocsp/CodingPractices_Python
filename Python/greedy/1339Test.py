word_count = int(input())
#2차원 배열
#len - index = 자릿수
word_list = []
for i in range(0, word_count):
    word_list.append(input().split())

print(word_list)