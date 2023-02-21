N = int(input())
numbers = list(map(int,input().split()))
prime_numbers = N

for i in numbers:
    if i == 1 :
        prime_numbers -= 1
    else:
        for j in range(2, i):
            if i % j == 0 :
              prime_numbers -= 1
              break
print(prime_numbers)