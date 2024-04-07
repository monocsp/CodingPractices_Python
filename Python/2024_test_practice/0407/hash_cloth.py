
def solution(n,m):
    selected = []
    printers(selected,n,m)




def printers(choice,n, m):
    if m == len(choice):
        for i in choice:
            print(' '.join(map(str, choice)))

    last_number = 0
    if len(choice) > 0:
        last_number = choice[-1]
    for j in range(last_number+1, n+1,1):
        choice.append(j)
        printers(choice, n, m)
        choice.remove(j)


if __name__ == "__main__":
    solution(3, 2)
