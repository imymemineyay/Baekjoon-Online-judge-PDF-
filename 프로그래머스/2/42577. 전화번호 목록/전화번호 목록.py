def solution(phone_book):
    answer = True
    phone_nums = {num:1 for num in phone_book}
    
    for p in phone_book:
        tmp = ''
        for k in p:
            tmp += k
            if tmp in phone_nums and tmp != p:
                answer = False

    return answer   