def solution(emergency):
    lst = sorted(emergency, reverse = True)
    answer = [lst.index(i)+1 for i in emergency]
    return answer