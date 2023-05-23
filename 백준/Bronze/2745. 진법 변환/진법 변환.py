from string import ascii_uppercase # 알파벳 생성

alph_list = list(ascii_uppercase) # 대문자 리스트로 만들기
lst = [str(i) for i in range(0,10)] # 0~9까지 리스트로 만들기

reference = lst + alph_list # 대문자 리스트와 소문자 리스트 결합
values = [j for j in range(0,36)] # reference에 해당하는 숫자 리스트 만들기

jinsu = dict(zip(reference, values)) # reference 랑 values 집합으로 만들기

N, B = input().split()
B = int(B)

result = 0
n = len(N) -1 
for k in N:
    result += jinsu[k] * B **n 
    n -= 1
print(result)