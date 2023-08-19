# 첫번째 수 
n = 1
lst = []

dn_s = []
for i in range(1, 10000):

  # d(i) 만들기
      dn = i + sum(list(map(int, list(str(i)))))
      dn_s.append(dn)

for i in range(1, 10000):
      if i not in dn_s:
            print(i)