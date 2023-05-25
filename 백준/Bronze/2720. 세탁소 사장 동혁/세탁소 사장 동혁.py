T = int(input())

change = [25,10,5,1]

for _ in range(T):
    C = int(input())
    give_it_to_customers = [0,0,0,0]
    i = 0
    while C > 0 :
          give_it_to_customers[i] = C//change[i]
          C = C % change[i]
          i += 1
    print(*give_it_to_customers)