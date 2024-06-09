def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        num = int(i[s:s+l])
        if num > k:
            answer.append(num)
    return answer