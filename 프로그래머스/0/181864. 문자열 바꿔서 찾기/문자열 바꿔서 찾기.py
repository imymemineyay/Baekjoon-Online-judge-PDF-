def solution(myString, pat):
    pat_new = ''
    for i in pat :
        if i == 'A':
            pat_new += 'B'
        else:
            pat_new += 'A'
    return 1 if pat_new in myString else 0