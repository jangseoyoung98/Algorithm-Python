def solution(arr, divisor):
    new_arr = sorted(arr)
    result = []
    for n in new_arr:
        if not n%divisor: result.append(n)
    if not len(result): return [-1]
    return result