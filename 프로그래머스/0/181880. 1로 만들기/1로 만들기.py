def solution(num_list):
    answer = [0] * len(num_list)
    for idx, i in enumerate(num_list):
        if i == 1 :
            pass 
        else:
            while i // 2 != 1:
                if i % 2 != 0:
                    i -= 1
                    i = i//2
                    answer[idx] += 1 
                else: 
                    i = i//2
                    answer[idx] += 1
            answer[idx] +=1
    return sum(answer)

