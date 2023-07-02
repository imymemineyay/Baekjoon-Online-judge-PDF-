x,y = map(int,input().split())

calculate_date = 0
day = 0 
date = ['MON','TUE','WED','THU','FRI','SAT','SUN']

for i in range(x+1):
  if i in [1,3,5,7,8,10,12]:
    calculate_date += 31
    days = 31
  elif i == 2:
    calculate_date += 28
    days = 28
  elif i in [4,6,9,11]:
    calculate_date += 30
    days = 30

for yoil in range(calculate_date - (days-y)):
  day += 1
  if day == 7:
    day -= 7 
print(date[day-1])