import string
def solution(age):
    lower_char = [i for i in string.ascii_lowercase]
    return ''.join([lower_char[int(i)] for i in str(age)])