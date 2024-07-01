def solution(order):
    answer = 0
    menu = {'americano':4500, 'latte':5000, 'anything':4500}
    for i in order:
        if 'latte' in i :
            answer += menu['latte']
        elif 'americano' in i :
            answer += menu['americano']
        else:
            answer += menu['anything']
    return answer