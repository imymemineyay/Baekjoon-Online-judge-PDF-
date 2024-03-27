from itertools import permutations


# 순열 확인 함수
def is_prime_number(number):
    if number == 0 or number == 1: # 0,1 은 소수가 아니다
        return False
    
    for i in range(2,number): # 1과 자기자신을 제외한 숫자들로 나누어 떨어지면 합성수다
        if not (number % i):
            return False
        
    return True # 나누어 떨어지지 않으면 소수다. 



def solution(numbers):
    answer = 0
    # 1. numbers에 있는 수들로 모든 자리수별로 만들 수 있는 모든 수들을 만든다. 
    johabs_set = set()
    for n in range(1,len(numbers)+1) :
        # 단, 같은 수가 있는 경우가 있으니 중복을 제거해줘야한다. 
        johabs_set.update(set(map(lambda x : int(''.join(x)), permutations(numbers,n))))

    for johab in johabs_set:
        if is_prime_number(johab):
            answer += 1
    return answer