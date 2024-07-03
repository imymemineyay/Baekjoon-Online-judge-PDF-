def solution(my_string):
    # "3 + 4 + 5 + 1 - 2"
    # +는 0으로 바꾸고 - 는 뒤의 숫자의 2배를 마이너스한 값 담기 
    lst = []
    my_string = my_string.split(' ')
    for idx, string in enumerate(my_string):
        if string == '+':
            lst.append(0)
        elif string == '-':
            lst.append(int(my_string[idx+1])*-2)
        else :
            lst.append(string)
        
    return sum(list(map(int, lst)))