def solution(my_string):
    answer = []
    my_string = my_string[::-1]
    for i in range(len(my_string)):
        answer.append(my_string[0:i+1][::-1])
    return sorted(answer)