def solution(array, commands):
    answer = []
    for command in commands:
        lst = array[command[0]-1:command[1]]
        lst = sorted(lst)
        answer.append(lst[command[2]-1])
    return answer