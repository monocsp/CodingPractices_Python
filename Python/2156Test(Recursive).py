
global wine_list

def function(n, is_Continuous = 0):
    if n < len(wine_list):
        if is_Continuous == 2:
            x = 0
        else:
            x = wine_list[n] + function(n + 1, is_Continuous=is_Continuous+1)
        print(f"x is {x}")
        if n+1 < len(wine_list):
            y = function(n + 1)
        else:
            y = 0
        print(f"y is {y}")

        if x > y:
            return x
        elif y > x:
            return y
        else:
            return x
    else:
        return 0
if __name__ == "__main__":
    wine_list = []
    test_count = int(input())
    for i in range(test_count):
        receive = int(input())
        wine_list.append(receive)
    print(function(0))

