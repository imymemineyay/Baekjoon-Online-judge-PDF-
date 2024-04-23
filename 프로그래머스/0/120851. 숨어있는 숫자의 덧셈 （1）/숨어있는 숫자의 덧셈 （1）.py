def solution(my_string):
    answer = [int(i) for i in my_string if i.isdigit()]
    return sum(answer)