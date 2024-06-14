def solution(array, n):
    array = sorted(array)
    lst = [abs(i - n) for i in array]
    idx = lst.index(min(lst))
    return array[idx]