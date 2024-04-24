def solution(my_string, num1, num2):
    num_1 = my_string[num1]
    num_2 = my_string[num2]
    answer = ''
    for idx, i in enumerate(my_string):
        if idx == num1:
            answer += num_2
        elif idx == num2:
            answer += num_1
        else:
            answer += i
    return answer