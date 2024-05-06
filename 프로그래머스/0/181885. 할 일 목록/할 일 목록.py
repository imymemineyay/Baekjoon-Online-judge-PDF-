def solution(todo_list, finished):
    answer =[]
    for idx, yesno in enumerate(finished):
        if yesno == False:
            answer.append(todo_list[idx])
    return answer