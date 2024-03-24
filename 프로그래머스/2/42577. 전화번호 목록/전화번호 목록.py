def solution(phone_book):
    answer = True
    pot = {}

    for i in phone_book:
        pot[i] = pot.get(i,1)

    # 번호가 다른 번호로 시작하는지 확인
    for k in pot:
        # 숫자 앞자리씩 가져와서 통에 들어있는지 확인 
        phone = ''
        for j in k :
            phone += j
            if phone in pot and phone != k:
                answer = False

    return answer 