def solution(my_string, m, c):
    answer = ''
    for i in list(range(len(my_string)))[::m]:
        answer += my_string[i:i+m+1][c-1]
    return answer
