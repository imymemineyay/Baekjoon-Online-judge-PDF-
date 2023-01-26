N = int(input())

floor = 1  # 1층 
num = 1 # 1층의 숫자

while True :
  if N <= num : # 층의 마지막 숫자
      print(floor)
      break
  else:
      num += (6 * floor) # 각 층의 마지막 숫자는 1 + 6의 배수들의 합
      floor +=1