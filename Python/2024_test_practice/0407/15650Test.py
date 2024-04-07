def dfs(start, end,count, selected):
    # print(f"start : {start} end : {end} count : {count} selected : {selected} ")
    if len(selected) == count:
        for i in selected:
            print(' '.join(map(str,selected) ))
            return

    else:
        for i in range(start, end+1, 1):
            # print(f"I : {i}")
            selected.append(i)
            # print(f"selected: {selected}")
            dfs(i, end, count, selected)
            selected.pop()


def solution(n, m):
    selected = []

    dfs(1,4, n, selected)



if __name__ == "__main__" :
    dfs(1,4,2,[])