n = int(input())
tot = 0

for i in range(1,n-1):
    tot += (i * (n-(i+1)))

print("""{}
3""".format(tot))