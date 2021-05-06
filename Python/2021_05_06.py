# #if 문제
#1번
# a,b = input().split()
# a = int(a)
# b = int(b)
# if(a<b):
#     print('<')
# elif(a>b):
#     print('>')
# else:
#     print('==')
#2번
# score = int(input())
# if(90<=score and score<=100):
#     print('A')
# elif(80<=score and 89>=score):
#     print('B')
# elif(70<=score and 79>=score):
#     print('C')
# elif(60<=score and 69>=score):
#     print('D')
# else:
#     print('F')
# #3번
# year = int(input())
# result = ((year%4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
# # if(result):
# #     print(1)
# # else:
# #     print(0)
# print(str(int(result)))
# # #4번
# x = input()
# y = input()
# resultX = int(x)>0
# resultY = int(y)>0
# if(resultX):
#     if(resultY):
#         print("1")
#     else:
#         print("4")
# else:
#     if(resultY):
#         print("2")
#     else:
#         print("3")
# # #5번
hh,mm = input().split()
hh = int(hh)
mm = int(mm)
if(mm <45):
    mm +=15
    if(hh == 0):
        hh = 23
    else:
        hh -=1
    print(str(hh) + ' ' + str(mm))
else:
    mm-= 45
    print(str(hh) + ' ' + str(mm))