import sys

N = int(sys.stdin.readline())
card = set(sys.stdin.readline().split())

M = int(sys.stdin.readline())
check_card = sys.stdin.readline().split()

# answer = []

for i in check_card:
  if i in card:
    # one = i.replace(i,'1')
    # answer.append(one)
    print(1, end= ' ')
  else:
    # zero = i.replace(i,'0')
    # answer.append(zero)
    print(0, end= ' ')
