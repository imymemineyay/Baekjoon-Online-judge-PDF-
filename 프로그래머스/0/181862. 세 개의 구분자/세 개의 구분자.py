def solution(myStr):
    ans = []
    lst = myStr.split('a')
    for i in lst:
        ans.extend(i.split('b'))
        
    answer = []
    for i in ans:
        answer.extend(i.split('c'))
    
    result = []
    for i in answer:
        if i != '':
            result.append(i)
    
    
    if len(result) == 0:
        result.append('EMPTY')
        
    return result
            