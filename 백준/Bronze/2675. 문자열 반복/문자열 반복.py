from posixpath import join
T = int(input())
for i in range(T):
    RS = input().split()
    New_RS = []
    for j in RS[1]:
        element = j * int(RS[0])
        New_RS.append(element)
    print(''.join(New_RS))