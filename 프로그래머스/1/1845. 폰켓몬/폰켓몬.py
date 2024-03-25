# N마리 폰켓몬 중 N/2 ok
# 종류에 따라 번호 부여
# 최대한 다양한 종류의 폰켓몬 가지길 원하기 때문에 많은 종류의 폰켓몬을 포함해 N/2마리 선택
# 폰켄못 종류번호가 담긴 배열 = nums
# 폰켓몬 종류 개수의 최댓값 하나만 return


# 포켓몬 종류는 여러개고 그 안에 겹치는 애도 있다.
# 그런데 내가 가지고 갈 수 있는 최대의 개수는 N/2 이다. 
# 그치만 N/2에는 겹치는 애들이 있을 수 있다. 
# 그래서 종류가 몇갠지 그것이 중요하다 왜냐 안겹치니까~!

def solution(nums): 
    answer = 0
    pot = {}
    for i in nums:
        pot[i] = pot.get(i,0)+1
    num_pocket_type = len(pot)
    max_products = len(nums)//2 
    
    if num_pocket_type >= max_products: 
        answer = max_products
    else: 
        answer = num_pocket_type
    return answer 
    
    
    


    