"""
한 명의 선수를 제외하고 모든 선수가 마라톤을 완주
participant : 모든 선수 이름이 담긴 통 
completion : 완주한 선수 이름이 담긴 통 
answer : 완주하지 못한 선수의 이름 담긴 통 

1. 완주하고 완주 못한 선수로 구분된 통을 만든다.

2. 모든 선수가 담긴 통에서 완주한 선수가 담긴 통을 제외한 나머지를 solution 통에 담는다.
   완주X = 전체 선수 - 완주한 선수 
   (1) 전체 선수의 이름과 그 이름에 해당하는 개수를 담은 통을 만든다
   (2) 1번에서 만든 통에 완주한 선수의 이름이 있으면 그 이름에 해당하는 -1 해준다. 
   (3) 개수가 1인 선수의 이름만 뽑는다. 
"""

def solution(participant, completion):
    answer = ""
    entire = {}
    for i in participant:
        entire[i] = entire.get(i,0) +1 

    for j in completion:
        entire[j] -= 1 

    # entire에 있는 value중 1이상인 key값을 뽑는것 
    for k in entire:
        if entire[k] >= 1:
            answer += k

    return answer