def solution(date1, date2):
    lst1 = ''.join(list(map(str, date1)))
    lst2 = ''.join(list(map(str, date2)))
    if int(lst1) < int(lst2):
        return 1 
    else: 
        return 0