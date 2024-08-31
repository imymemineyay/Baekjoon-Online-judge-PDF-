def solution(numbers):
    number_lst = ['zero','one', 'two', 'three', "four", "five", 
                  "six", "seven", "eight", "nine" ]
    answer = ""
    alphabet = ""
    for num in numbers:
        alphabet += num
        if alphabet in number_lst:
            answer += str(number_lst.index(alphabet))
            alphabet = ""

    return int(answer)