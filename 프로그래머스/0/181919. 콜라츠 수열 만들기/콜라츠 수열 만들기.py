def solution(n):
    answer = [n]
    while n > 1:
        if n % 2 == 0:
            n /= 2
            answer.append(n)
        else: 
            n = n*3 + 1
            answer.append(n)
    return answer