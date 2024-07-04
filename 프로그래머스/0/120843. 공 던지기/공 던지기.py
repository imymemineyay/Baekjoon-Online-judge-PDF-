def solution(numbers, k):
    numbers = numbers * k 
    num = 0 
    for i in range(0,len(numbers),2):
        if num <= k-1:
            answer = numbers[i]
            num += 1 
        else : 
            return answer