def solution(num_list):
    answer_1 = ''
    answer_2 = ''
    for i in num_list:
        if i % 2 == 0:
            answer_1 += str(i)
        else:
            answer_2 += str(i)
    return int(answer_1) + int(answer_2)
