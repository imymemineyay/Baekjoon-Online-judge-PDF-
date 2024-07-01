def solution(q, r, code):
    answer = ''
    for idx,num in enumerate(code):
        if idx % q == r :
            answer += num
    return answer