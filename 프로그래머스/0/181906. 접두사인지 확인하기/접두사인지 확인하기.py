def solution(my_string, is_prefix):
    num = len(is_prefix)
    if my_string[:num] == is_prefix:
        return 1
    else:
        return 0
