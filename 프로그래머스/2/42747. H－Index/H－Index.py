def solution(citations):
    answer=0
    # 1. 논문의 피인용수를 내림차순 정렬한다.
    citations.sort(reverse=True)

    # 2. 논문의 갯수보다 피인용수가 같거나 작아질때 그때가 h_index의 수이다. 
    for i in range(len(citations)):
        if citations[i] < i+1:
            break
        else:
            answer +=1
    return answer

'''
h-index를 나타내는 h값을 구하는 문제

과학자 발표 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고, 
나머지가 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-index
'''