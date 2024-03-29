def solution(answers):
    answer = []
    answers = list(map(str,answers))

    number_1 = '12345' * 2000
    number_2 = '21232425' * (10000//8)
    number_3 = '3311224455' * 1000

    correct_cnt = [0,0,0]

    for idx, num in enumerate(answers):
        if num == number_1[idx]:
            correct_cnt[0] += 1
        if num == number_2[idx]:
            correct_cnt[1] += 1
        if num == number_3[idx]:
            correct_cnt[2] += 1


    max_score = max(correct_cnt)

    for idx, score in enumerate(correct_cnt):
        if score == max_score:
            answer.append(idx+1)
    return answer