def solution(my_string, queries):
    answer = []
    my_string = list(my_string)
    for idx_1, idx_2 in queries :
        answer = my_string[idx_1:idx_2+1][::-1]
        my_string[idx_1:idx_2+1] = answer
    return ''.join(my_string)