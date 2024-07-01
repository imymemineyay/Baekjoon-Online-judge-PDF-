def solution(arr):
    answer = 0
    arr_present = arr.copy()
    arr_after = arr_present.copy()
    while True:
        for idx, num in enumerate(arr_after):
            if num >= 50 and num % 2 == 0 :
                arr_after[idx] = num % 2 
            elif num < 50 and num % 2 != 0 :
                arr_after[idx] = (num * 2) + 1 
        if arr_present == arr_after :
            return answer 
        else :
            arr_present = arr_after.copy()
            answer+= 1 