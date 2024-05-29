def solution(a, b, c):
    if a != b and b != c and a != c:
        return a+b+c
    elif (a == b and b != c) or (b==c and a!= c) or (c==a and a!=b):
        return (a+b+c) * (a**2 + b**2 + c**2)
    else:
        return (a+b+c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
