def solution(phone_book):
    answer = True
    
    # 전체 번호가 담긴 통을 준비한다. 
    phone_nums = {}
    for i in phone_book:
        phone_nums[i] = phone_nums.get(i,0)+1
        
    # 앞서 만든 통 중 번호를 하나씩 뽑아서 변수에 담는다.
    for phone in phone_nums:
        num = ''
    # 해당 번호가 전체 번호에 있는지 확인한다. 단, 자기자신과는 다른 번호여야한다. 
        for j in phone:
            num += j
            if num in phone_nums and num != phone:
                answer = False
                break
    return answer 