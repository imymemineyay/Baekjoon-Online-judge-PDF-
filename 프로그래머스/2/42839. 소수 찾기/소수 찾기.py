def solution(numbers):
    answer = 0
    # 1. 받은 숫자를 permutations를 이용하여 조합을 만든다. 
    from itertools import permutations

    number_lst = []
    # 2. 단 같은 수가 많아지니 집합함수로 중복제거를 해준다. 
    for n in range(1,len(numbers)+1) :
        johabs = permutations(numbers,n)
        for johab in johabs:
            number_lst.append(int(''.join(johab)))

    number_lst = set(number_lst)

    # 3. 소수는 1과 자신 외에 다른 수와 나눠질 수 없으니까 1과 자기자신 외의 수로 나누고 만약 나눠지는게 있으면 해당 
    for num in number_lst:
        cnt = 0
        if num != 0 or num != 1:
            for i in range(1,num):
                if int(num) % i == 0:
                    cnt += 1
                    if cnt == 2:
    # 작업 중지하고 다음 일 진행 
                        break
    # 4. 소수인 것은 cnt해준다. 
            if cnt == 1:
                answer += 1 
    return answer