T = int(input())

for i in range(T):
    text = input()
    if len(text) == 1 :
        print(text * 2)
    else:
        print(text[0] + text[-1])