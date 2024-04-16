def solution(my_string, n):
    answer = ''.join( i*n for i in my_string)
    return answer