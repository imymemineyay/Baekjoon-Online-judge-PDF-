def solution(clothes):
    answer = 1
    clothing = {}
    for item in clothes:
        type = item[1]
        clothing[type] = clothing.get(type,0) + 1

    for item in clothing:
        answer *= (clothing[item]+1)

    answer -= 1
    return answer