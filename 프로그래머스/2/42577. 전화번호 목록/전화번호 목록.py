def solution(phone_book):
    answer = True
    
    phone_book_dic = dict()
    for i in phone_book:
        phone_book_dic[i] = phone_book_dic.get(i,1)

    # 1. 전화번호부에 있는 번호를 하나씩 추출한다.
    for phone in phone_book_dic:
        # 번호의 첫번째 숫자부터 마지막 숫자까지 차례대로 추출하고 번호를 만들어 준다.
        number = ''
        for num in phone:
            number += num
            # 이 번호가 만약 전화번호부에 있으면서 자기자신이 아닐 경우, 
            if number in phone_book_dic and number != phone:
                # False를 반환하고 중단한다.
                answer = False
                break
    return answer 