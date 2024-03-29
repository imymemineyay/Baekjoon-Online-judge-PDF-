def solution(citations):
    answer=0
    cnt = 0
    # 1. 논문의 인용 횟수를 내림차순 정렬한 후, 하나씩 추출한다. 
    sorted_citations = sorted(citations, reverse=True)
    for i in sorted_citations:
    # 2. 인용 횟수와 몇 편째인지 함께 구해준다.
        if cnt < i:
            cnt +=1
    # 3. 인용 횟수가 h편 미만이면 다음 작업을 멈춘다.
        elif cnt > i:
            break

    # 4. 몇편째인지를 반환한다. 
    answer = cnt
    return answer

'''
h-index를 나타내는 h값을 구하는 문제

과학자 발표 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고, 
나머지가 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-index
'''