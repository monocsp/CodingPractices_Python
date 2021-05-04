# #백준 단계별 문제풀기 1일차
# #1번문제
# print("Hello World!")
# #2번 문제
# print("강한친구 대한육군")
# print("강한친구 대한육군")
# #3번 문제
# print("\    /\\ ")
# print(" )  (   ')")
# print("(  /  )")
# print(" \(__)|")
#5번 문제
# a,b = input().split()
# a = int(a)
# b = int(b)
# print(a+b)
#6번 문제
# a,b = input().split()
# a = int(a)
# b = int(b)
# print(a-b)
#7번 문제
# a,b = input().split()
# a = int(a)
# b = int(b)
# print(a*b)
#8번 문제
# a,b = input().split()
# a= float(a)
# b = float(b)
# print(a/b)
#9번 문제
# a,b = input().split()
# a = int(a)
# b = int(b)
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)
#10번 문제
# a,b,c = input().split()
# a = int(a)
# b = int(b)
# c = int(c)
# print((a+b)%c)
# print(((a%c) + (b%c))%c)
# print((a*b)%c)
# print(((a%c) * (b%c))%c)
#11번 문제
# a = input()
# b = input()
# print(int(a)*int(b[2]))
# print(int(a)*int(b[1]))
# print(int(a)*int(b[0]))
# print(int(a)*int(b))
#1002번 문제
test_count = int(input())
test_result = []
while test_count >0:
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    distance = ((x1-x2)**2 + (y1-y2)**2)**0.5
    sum_radius = float(r1+r2)
    if(sum_radius>distance):
        large = 0
        if(r1>r2):
            large = r1
        else:
            large = r2
        if(large > distance):
            test_result.append(0)
        else:
            test_result.append(2)
    elif(sum_radius < distance):
        test_result.append(0)
    else:
        test_result.append(1)
    test_count -= 1
for result in test_result:
    print(result)