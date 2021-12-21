def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i-1) + fibonacci(i-2)
if __name__ == "__main__":
    receive_input = int(input())
    print(fibonacci(receive_input))