grades = {'A+': 4.5 , 'A0': 4.0, 'B+':3.5, 'B0' :3.0, 'C+':2.5, 
         'C0':2.0, 'D+':1.5, 'D0':1.0, 'F': 0.0, 'P': 0.0}
score_X_gpa = [] # 학점 * 과목 평점의 합을 구하기 위한 리스트
sum_scores = [] # 학점 총합을 구하기 위한 리스트

for _ in range(20): # 20 줄
    class_name, score, grade = input().split() # 과목, 학점, 등급
    
    if grade == 'P':
        score = 0.0
    else: 
        score = float(score) # 학점 소수점화 
    score_X_gpa.append(score*grades[grade])
    sum_scores.append(score)

GPA = sum(score_X_gpa) / sum(sum_scores) 
print('%.6f'%GPA) # 소수점 이하 6자리