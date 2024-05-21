def solution(numbers):
    numbers = sorted(numbers)
    num1 = numbers[0] * numbers[1]
    num2 = numbers[-2] * numbers[-1]
    return num1 if num1  >= num2 else num2