number = input().split()

A = ''.join(list(reversed(number[0])))
B = ''.join(list(reversed(number[1])))

A = int(A)
B = int(B)

print(max(A,B))