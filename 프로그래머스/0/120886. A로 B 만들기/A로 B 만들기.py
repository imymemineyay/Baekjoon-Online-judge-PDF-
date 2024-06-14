def solution(before, after):
    dic_before = {}
    for i in before:
        dic_before[i] = dic_before.get(i,0)+1 
        
    dic_after = {}
    for i in after:
        dic_after[i] = dic_after.get(i,0)+1 
    
    return(int(dic_before == dic_after))
