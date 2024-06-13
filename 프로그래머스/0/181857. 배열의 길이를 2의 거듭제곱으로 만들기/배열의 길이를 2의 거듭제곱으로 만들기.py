import math

def solution(arr):
    length = len(arr)
    add_length = 2 ** math.ceil(math.log2(length))
    adding = add_length - length
    return arr + [0] * adding
    