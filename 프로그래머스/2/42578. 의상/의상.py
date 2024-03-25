def solution(clothes):
    answer = 1
    
    # 종류별로 옷이 몇 개 있는지 알 수 있는 통을 만든다. 단, 옷의 개수에 +1을 해줘서 없는 것 까지 고려한다. 
    clothing = {}
    for idx in clothes:
        i = idx[1]
        clothing[i] = clothing.get(i,1) +1     
    # 종류별 옷의 개수를 곱해준 후 모든 옷을 안입었을 경우의 경우의 수를 빼준다. 
    for type in clothing:
        answer *= clothing[type]
    answer -= 1
    return answer