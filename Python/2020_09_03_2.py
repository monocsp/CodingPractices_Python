#problem url : https://www.acmicpc.net/problem/15552
import sys
import random

def looping(count):
    for i in range(0, count):
        a = random.randint(0,1000)
        b = random.randint(0,1000)
        print('{} \t {}'.format(a, b))
        list.append(a+b)
    print(list)

if __name__ == '__main__':
    count = int(sys.stdin.readline())
    looping(count)
