def solution(my_string):
    for i in my_string:
        if i.isnumeric() == False:
            my_string = my_string.replace(i,' ')
    
    answer = 0
    for i in my_string.split(' '):
        if i.isnumeric():
            answer += int(i)
    return answer
