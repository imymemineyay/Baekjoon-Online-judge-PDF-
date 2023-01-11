from string import ascii_lowercase

S = input()
alphabet_lst = list(ascii_lowercase)

for i in alphabet_lst:
  if i not in S:
    a = alphabet_lst.index(i)
    alphabet_lst[a] = -1
  elif i in S:
    a = alphabet_lst.index(i)
    b = S.index(i)
    alphabet_lst[a] = b
  print(alphabet_lst[a], end=' ')


    