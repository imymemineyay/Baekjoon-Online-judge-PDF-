def solution(my_string, alp):
    answer = ''.join(i.upper() if i == alp else i for i in my_string )
    return answer