def solution(board, k):
    answer = 0
    for idx, num in enumerate(board):
        for idx2, num2 in enumerate(num):
            if idx + idx2 <=k:
                answer += num2
    return answer