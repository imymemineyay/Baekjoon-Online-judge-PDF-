def solution(array, n):
    answer = 0
    lst = [0] * (max(array) +1)

    for i in array:
        lst[i] += 1

    answer = lst[n]
    return answer