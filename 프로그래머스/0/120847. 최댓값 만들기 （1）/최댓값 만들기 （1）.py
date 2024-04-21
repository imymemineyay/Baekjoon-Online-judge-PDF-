def solution(numbers):
    numbers = sorted(numbers, reverse = True)
    answer = numbers[0] * numbers[1]
    return answer