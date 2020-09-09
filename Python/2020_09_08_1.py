import sys

def Drawstar(depth):
    count = depth
    space = 0
    if count > 0 :
        for i in space:
            print(' ')
        for i in count:
            print('*')
        print('\n')
        space += 1
        count -= 1
    else :
        for i in space:
            print(' ')
        for i in count:
            print('*')



if __name__ == '__main__':
    count = int(sys.stdin.readline())
    print(count)