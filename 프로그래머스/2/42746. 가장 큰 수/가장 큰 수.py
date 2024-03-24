def solution(numbers):
    # 1. 조건이 1000이하이니 모든 백단위로 맞춰준 숫자와 새로 만든 수가 담긴 통을 만든다.
    number_ranking = {}
    answer = ''
    for num in numbers:
        if num < 10:
            number_ranking[num] = number_ranking.get(num, num * 100)
        elif num < 100:
            number_ranking[num] = number_ranking.get(num, num * 10)
        else:
            number_ranking[num] = number_ranking.get(num, num)

    # 2. 통을 새로 만든 수를 기준으로 정렬해준다.
    result_ranking = sorted(number_ranking, key=lambda x: number_ranking[x], reverse=True)

    # 3. 리스트 안의 수를 출력한다.
    for i in result_ranking:
        if answer == '':
            answer = '0' if i == 0 else str(i)
        else:
            answer += str(i)

    return answer
def solution(numbers):
    # 주어진 숫자들을 문자열로 변환합니다.
    numbers = list(map(str, numbers))
    
    # 숫자를 두 번 이어붙여 비교하여 더 큰 순서로 정렬합니다.
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    # 리스트의 모든 요소를 이어붙여 문자열로 반환합니다.
    answer = str(int(''.join(numbers)))
    
    return answer