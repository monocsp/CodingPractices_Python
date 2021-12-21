global fibo_list

def fibonacci(n):
    if fibo_list[n] != 0:
        return fibo_list[n]
    else:
        fibonacci(n-1)
        fibonacci(n-2)
        fibo_list[n] = [fibo_list[n-1][0]+fibo_list[n-2][0], fibo_list[n-1][1]+fibo_list[n-2][1]]

if __name__ == "__main__":
    fibo_list = [[1,0],[0,1]]
    fibo_list.extend([0 for i in range(39)])
    test_count = int(input())
    result_list = []
    for i in range(test_count):
        fino_count = int(input())
        fibonacci(fino_count)
        result_list.append(fibo_list[fino_count])

    for i in result_list:
        print(f"{i[0]} {i[1]}")




