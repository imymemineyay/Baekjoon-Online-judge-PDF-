def solution(clothes):
    answer = 1
    # clothes의 요소를 일일이 추출하며
    item_num = dict()
    for item in clothes:
    #     딕셔너리에 종류별로 몇개의 아이템이 있는지 담는다.
        item_num[item[1]] = item_num.get(item[1],0) + 1

    # 딕셔너리에 있는 요소를 일일이 추출하며 
    for ele in item_num:
    #     각 종유별로 몇 개의 아이템이 있는지 구한다. 아이템의 개수 +1한 수를 answer에 곱해준다. 
        answer *= item_num[ele] +1 

    # 마지막에 answer -1 을 해준다.
    answer -= 1 
    return answer