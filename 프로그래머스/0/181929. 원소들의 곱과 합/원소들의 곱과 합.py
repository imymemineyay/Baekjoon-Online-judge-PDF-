from math import prod

def solution(num_list):
    com_1 = prod(num_list) 
    com_2 = sum(num_list) ** 2 
    if com_1 < com_2:
        return 1
    else:
        return 0