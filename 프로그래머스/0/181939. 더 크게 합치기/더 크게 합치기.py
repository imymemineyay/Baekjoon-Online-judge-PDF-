def solution(a, b):
    a_b = int(str(a)+str(b))
    b_a = int(str(b)+str(a))
    return a_b if a_b >= b_a else b_a