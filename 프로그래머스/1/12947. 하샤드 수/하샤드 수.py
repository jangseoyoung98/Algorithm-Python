def solution(x):
    sum_x = 0
    str_x = str(x)
    for l in str_x:
        sum_x += int(l)
    
    if not x%sum_x: return True
    
    return False