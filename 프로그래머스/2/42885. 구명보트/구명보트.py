from collections import deque


def solution(people, limit):
    answer = 0
    people = sorted(people, reverse=True)
    people_in_island  = deque(people)
    
    boat = 0
    for person in list(people_in_island):
        if len(people_in_island) > 1:
            if person + people_in_island[-1] <= limit:
                boat += 1
                people_in_island.popleft()
                people_in_island.pop()
            elif person <= limit:
                boat += 1
                people_in_island.popleft()
            else:
                people_in_island.popleft()
        elif len(people_in_island) == 1:
            if person <= limit:
                boat += 1
                people_in_island.popleft()
            else:
                people_in_island.popleft()
        else:
            break
    answer = boat

    return answer