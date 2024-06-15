def solution(strArr):
    dic = dict()
    for i in strArr:
        length = len(i)
        dic[length] = dic.get(length,0) + 1
    
    return max(dic.values())
