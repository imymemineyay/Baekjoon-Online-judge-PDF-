def solution(s):
    s = s.split(' ')
    answer = [0]
    for idx, num in enumerate(s) :
        if num == 'Z':
            answer = answer[:-1]
        else:
            answer.append(num)
            
    return sum(list(map(int, answer)))