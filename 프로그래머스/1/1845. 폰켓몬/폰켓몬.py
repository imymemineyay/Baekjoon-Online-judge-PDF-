# 총 N마리의 폰켓몬 중 N/2마리 가져갈 수 있음
# 폰켓몬은 종류에 따라 번호를 붙여 구분함 
# 최대한 다양한 종류가 담긴 N/2마리의 폰켓몬을 가져가고자 함
# N/2마리의 폰켓몬 중 최대한 다른 종류의 폰켓몬의 수를 구하라 

def solution(nums): 
    answer = 0
    # 폰켓몬의 종류가 몇 갠지 확인한다.
    type_cnt = len(set(nums))
    # 가져갈 수 있는 폰켓몬 수를 구한다. 
    max_cnt = len(nums) // 2 
    # 폰켓몬 종류는 몇 마리 
    answer = min(type_cnt, max_cnt)
    return answer 
    
    
    


    