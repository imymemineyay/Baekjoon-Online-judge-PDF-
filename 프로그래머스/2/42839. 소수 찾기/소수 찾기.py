from itertools import permutations


# 순열 확인 함수
def is_prime_number(num):
    if num == 0 or num == 1:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True



def solution(numbers):
    answer = 0
    num_set = set()
    for i in range(1, len(numbers)+1):
        shu = list(map(lambda x: int(''.join(x)),list(permutations(numbers, i))))
        num_set.update(shu)

    for n in num_set:
        if is_prime_number(n):
            answer += 1

    return answer