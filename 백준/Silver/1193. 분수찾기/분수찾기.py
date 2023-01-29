X = int(input())

last_num = 1  # line 내의 마지막 번호 
line = 1 #  대각선 번호

# X가 위치한 line 구하기
while True:
  if X <= last_num :
      line   # tot는 line의 번호 
      break
  else:
      line += 1
      last_num += line

# line의 번호를 이용하여 X번째 분수 구하기
if line % 2 == 0 : # line이 짝수일 경우 분모가 1씩 줄어듦
    top = 1
    bottom = line
    for i in range(last_num - line + 1, last_num + 1): # line 내의 숫자의 번호와 매치시키기
        if X == i:
            break
        else:
            top += 1
            bottom -= 1  

else : # line이 홀수일 경우 분자가 1씩 줄어듦
    top = line
    bottom = 1
    for i in range(last_num - line + 1, last_num + 1): # line 내의 숫자의 번호와 매치시키기
        if X == i:
            break
        else:
            top -= 1
            bottom += 1 

print('{0}/{1}'.format(top, bottom))