N, M = map(int,input().split())
cards = list(map(int,input().split()))
max_tot = 0

for first_idx in range(len(cards)-2):
    for second_idx in range(first_idx+1,len(cards)-1):
        for third_idx in range(second_idx+1, len(cards)):
            tot = cards[first_idx] + cards[second_idx] + cards[third_idx]
            if max_tot < tot and tot <= M:
                max_tot = tot 

print(max_tot)        