n = 0
lst = []

dns = []
for i in range(1, 10000):

  # make d(i)

  dn = i + sum(list(map(int, list(str(i)))))
  dns.append(dn)

for i in range(1, 10000):
  if i not in dns:
    print(i)