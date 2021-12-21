def findmax():
    max_count = None
    max_number = None
    for i in range(0,9):
        receive_num = int(input())
        if max_count is None or int(max_number) <receive_num:
            max_count = i+ 1
            max_number = receive_num
    print(max_number)
    print(max_count)

if __name__ == "__main__":
    findmax()
