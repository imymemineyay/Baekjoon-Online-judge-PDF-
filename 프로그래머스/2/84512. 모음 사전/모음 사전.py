def solution(word):
    answer = 0
    from itertools import product
    characters = 'AEIOU'
    dictionary = []

    # 컴비네이션 이용해서 단어의 모든 조합 만들기
    for i in range(1,6):
        words = product(characters, repeat=i)
        for j in words:
            dictionary.append(''.join(j))

    # 정렬하기 
    dictionary = sorted(dictionary)

    # index()를 활용해서 단어의 위치 찾기
    answer = dictionary.index(word) +1
    return answer