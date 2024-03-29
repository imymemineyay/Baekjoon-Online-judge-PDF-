def solution(n, lost, reserve):
    answer = 0
    # 학생별 체육복 수가 담긴 배열 생성
    students = [1]*(n+2)
    for l in lost:
        students[l] -= 1
    for r in reserve:
        students[r] += 1



    cnt = 0
    for idx, num in enumerate(students):
        if (num == 0 and students[idx-1] >=2):
            students[idx] +=1
            students[idx-1] -= 1
        elif (num == 0 and students[idx+1] >= 2):
            students[idx] += 1
            students[idx+1] -= 1


    for i in students[1:len(students)-1]:
        if i >= 1:
            answer += 1
    return answer