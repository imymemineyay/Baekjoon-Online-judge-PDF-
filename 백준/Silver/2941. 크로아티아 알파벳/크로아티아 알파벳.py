words = input()

croatia_alphabet = ['c=','c-','dz=','d-','lj','nj','s=','z=']
num_lst = []
word = []


for i in croatia_alphabet:
    if i in words:
        num = words.count(i)
        num_lst.append(num)
        word.append(i)
        words = words.replace(i,',')

words = words.replace(',','')
print(len(words)+sum(num_lst))