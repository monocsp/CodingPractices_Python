def findmaxmin():
    size = int(input())
    maxnumber = None
    minnumber = None
    numArr = input().split()
    max(numArr)
    for i in numArr:
        if minnumber is None or int(minnumber) > int(i):
            minnumber = i
        if maxnumber is None or int(maxnumber) < int(i):
            maxnumber = i

    print(f"{minnumber} {maxnumber}")


if __name__ == "__main__":
    findmaxmin()
