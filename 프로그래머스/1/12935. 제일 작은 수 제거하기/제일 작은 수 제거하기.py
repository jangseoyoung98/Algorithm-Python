def solution(arr):
    i = arr.index(min(arr))
    answer = arr
    answer.pop(i)
    if not answer: return [-1]
    return answer