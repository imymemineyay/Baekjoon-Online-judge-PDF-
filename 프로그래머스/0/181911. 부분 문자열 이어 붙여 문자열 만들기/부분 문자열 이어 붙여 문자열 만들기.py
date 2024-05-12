def solution(my_strings, parts):
    answer = ''
    for idx, i in enumerate(parts):
        answer += my_strings[idx][i[0]: i[1]+1]
    return answer