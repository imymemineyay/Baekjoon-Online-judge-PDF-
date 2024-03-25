def solution(answers):
    answer = []
    cnt = len(answers)	

    answer = []
    # 1. 1~3번 수포자의 정답지를 만든다.
    suhak_hater=[]
    suhak_hater.append(['12345'*2000][0][:cnt]) # 1번 
    suhak_hater.append(['21232425'*(10000//8)][0][:cnt]) # 2번
    suhak_hater.append(['3311224455' * (1000)][0][:cnt]) # 3번

    # 2. 답안지를 문자형으로 변환시켜준다.
    answers = ''.join(list(map(str,answers)))


    # 2. 수포자의 정답지와 실제 정답지를 일일히 비교하여 정답을 맞힌 갯수를 통에 담는다.
    correct_num = []
    for name, pick_num in enumerate(suhak_hater):
        correct_cnt = 0
        for idx, num in enumerate(answers):
            if num == pick_num[idx]:
                correct_cnt += 1
            else: correct_cnt += 0
        correct_num.append([name,correct_cnt])   

    # 3. 갯수를 기준으로 정렬하고, 만약 같은 값이 여러개라면 이름을 기준으로 오름차순 해준다.
    correct_num = sorted(correct_num,key=lambda x: (-x[1], x[0]))

    if correct_num[0][1] == correct_num[1][1] == correct_num[2][1]:
        answer = [correct_num[i][0]+1 for i in range(3)]
    elif correct_num[0][1] == correct_num[1][1] != correct_num[2][1]: 
        answer = [correct_num[i][0]+1 for i in range(2)]
    else:
        answer = [correct_num[0][0]+1]
    return answer