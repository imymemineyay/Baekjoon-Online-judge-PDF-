dial = input()

alphabet_lst = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
dial_number = []
for i in dial:
    for j in alphabet_lst:
        if i in j :
            number = alphabet_lst.index(j) + 3
            dial_number.append(number)
        else:
            number = 0
            dial_number.append(number)

print(sum(dial_number))