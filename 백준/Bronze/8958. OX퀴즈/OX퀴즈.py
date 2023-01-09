N = int(input())

lst = [input() for i in range(N)]



for i in lst:
  score = 0
  total_score = 0
  for k in i:
    if k == 'O':
      score += 1
      total_score += score 
    else:
      score = 0
  print(total_score)