def factorial(i):
    if i == 0 or i == 1:
        return 1
    else:
        return factorial(i-1) * i

if __name__ == "__main__":
    receive_input = int(input())
    print(factorial(receive_input))