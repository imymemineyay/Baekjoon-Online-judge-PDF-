def solution(myString, pat):
    answer = ''
    for idx,string in enumerate(myString):
        if myString[idx:idx+len(pat)] == pat:
            answer = myString[:idx+len(pat)]
    return answer