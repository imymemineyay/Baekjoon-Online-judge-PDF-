def solution(array):
    answer = 0
    array = sorted(array)
    answer = array[len(array)//2]
    return answer