def solution(people, limit):
    answer = 0
    sorted_desc_people = sorted(people, reverse =True)
    cnt=0

    for idx, i in enumerate(sorted_desc_people):
        if i + sorted_desc_people[-1] <= limit:
            cnt += 1
            sorted_desc_people.pop()
        elif (i + sorted_desc_people[-1] > limit) & i <= limit:
            cnt+=1
        else:
            continue

    answer = cnt
    return answer