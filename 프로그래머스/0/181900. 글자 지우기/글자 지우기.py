def solution(my_string, indices):
    ans = []
    for idx, num in enumerate(my_string):
        if idx not in indices:
            ans.append(num)
    return ''.join(ans)
