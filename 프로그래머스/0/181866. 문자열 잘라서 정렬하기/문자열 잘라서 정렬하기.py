def solution(myString):
    answer = sorted(myString.split('x'))
    lst = []
    for i in answer:
        if i:
            lst.append(i)
    return lst