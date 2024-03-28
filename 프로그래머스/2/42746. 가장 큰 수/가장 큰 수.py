def solution(numbers):
    answer = ''
    
    i = len(numbers)
    # 1. numbers의 요소를 문자 타입으로 변경한다.  
    numbers = list(map(str,numbers))
    # 2. 똑같은 수를 (i-1)만큼 반복한 수를 기준으로 numbers를 정렬한다. 
    sorted_numbers = sorted(numbers, key = lambda x : x*3, reverse=True)
    # 3. 정렬된 배열을 정수로 바꿔준 후 문자열로 변경한다. 
    answer = str(int(''.join(sorted_numbers)))

    return answer