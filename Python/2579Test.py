# def function(stair_list, n):
#     if n > 3:
#         a = stair_list[n-1] + stair_list[n-2] + function(stair_list[:n-4], len(stair_list[:n-4]))
#         b = stair_list[n-1] + stair_list[n-3] + function(stair_list[:n-4], len(stair_list[:n-4]))
#         if a > b:
#             return a
#         else:
#             return b
#     else:
#         if n == 3:
#             a = stair_list[2] + stair_list[1]
#             b = stair_list[2] + stair_list[0]
#             if a > b:
#                 return a
#             else:
#                 return b
#         elif n == 2:
#             return stair_list[1] + stair_list[0]
#         elif n == 1:
#             return stair_list[0]
#
#
def solution(arr1, arr2):
    answer = []
    for i in range(0, len(arr1)):
        result_list = []
        for j in range(0, len(arr1[i])):
            result_list.append(arr1[i][j] + arr2[i][j])
        answer.append(result_list)

    return answer

if __name__ == "__main__":
    test = [1,2,2,2,2]
    print(test.index(max(test)))






#     stair = []
#     stair_height = int(input())
#     for i in range(0, stair_height):
#         stair_score = int(input())
#         stair.append(stair_score)
#     print(function(stair, stair_height))
