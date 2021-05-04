import sys



if __name__ == '__main__':
    numbers = list(map(int,input("hi").split()))

    i, temp = 0,0
    for i in range(len(numbers)):
        j = i+1
        for j in range(len(numbers)):
            if(numbers[i]< numbers[j]):
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp
                print("2 i is " + str(i))
                print("2 j is " +str(j))
                print(numbers)
    for i in range(len(numbers)):
        print(numbers[i], end = " ")
