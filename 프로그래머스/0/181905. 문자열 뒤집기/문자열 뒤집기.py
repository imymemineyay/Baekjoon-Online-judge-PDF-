def solution(my_string, s, e):
    print(my_string[:0])
    return my_string[:s] + my_string[e:s:-1] +my_string[s] + my_string[e+1:]