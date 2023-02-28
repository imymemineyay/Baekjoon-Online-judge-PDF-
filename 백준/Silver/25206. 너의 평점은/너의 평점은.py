score_X_gpa = [] # 학점 * 과목 평점의 합을 구하기 위한 리스트
sum_scores = [] # 학점 총합을 구하기 위한 리스트

for _ in range(20): # 20 줄
    class_name, score, grade = input().split() # 과목, 학점, 등급
    score = float(score) # 학점 소수점화 

    ## 등급별 과목평점 지정
    if grade == 'A+':
        gpa = 4.5 * score
        num = score
    elif grade == 'A0':
        gpa = 4.0 * score
        num = score
    elif grade == 'B+':
        gpa = 3.5 * score
        num = score
    elif grade == 'B0':
        gpa = 3.0 * score
        num = score
    elif grade == 'C+':
        gpa = 2.5 * score
        num = score
    elif grade == 'C0':
        gpa = 2.0 * score
        num = score
    elif grade == 'D+':
        gpa = 1.5 * score
        num = score
    elif grade == 'D0':
        gpa = 1.0 * score
        num = score
    elif grade == 'F':
        gpa = 0.0 * score
        num = score
    elif grade == 'P': 
        gpa = 0.0
        num = 0.0
    score_X_gpa.append(gpa)
    sum_scores.append(num)

GPA = sum(score_X_gpa) / sum(sum_scores) 
print('%.6f'%GPA)