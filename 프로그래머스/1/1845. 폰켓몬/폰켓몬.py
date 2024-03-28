def solution(nums): 
    answer = 0
    # nums에서 폰켓몬의 종류가 몇 개가 있는지 구한다.
    nums_set = set(nums)
    num_type = len(nums_set)

    # 가질 수 있는 폰켓몬의 개수(n/2)를 구한다. 
    num_phoneketmon = len(nums)//2

    # 가질 수 있는 폰켓몬 수와 종류의 개수를 비교해서 작은 값을 반환한다.
    answer = min(num_type, num_phoneketmon)
    return answer 
    
    
    


    