#LL을 하나의 자리세트라고 한다면,
#컵홀더 갯수 = 자리세트 + 1
#전부 S -> 컵홀더 1개가 남음 ; return len(s)
#1개의 커플석 나머지 S -> 컵홀더 딱 맞음 ; return len(s) + len(LL)
# n>1, m>1, n개의 커플석, m개의 S석 : return 컵홀더 갯수

sit_count = int(input())
sit_position = input()

s_count = sit_position.count('S')
LL_count = (sit_count - s_count)//2

if LL_count == 0:
    print(s_count)
elif LL_count == 1:
    print(sit_count)
else:
    print(s_count+LL_count+1)
