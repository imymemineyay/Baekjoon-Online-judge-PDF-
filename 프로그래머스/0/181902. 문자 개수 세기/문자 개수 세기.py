import string 

def solution(my_string):
    alphabet_lst = [i for i in string.ascii_uppercase]
    alphabet_lst.extend([i for i in string.ascii_lowercase])
    alphabet_dic = dict(zip(alphabet_lst, [0]*52))   
    
    for i in my_string :
        alphabet_dic[i] += 1
    return list(alphabet_dic.values())