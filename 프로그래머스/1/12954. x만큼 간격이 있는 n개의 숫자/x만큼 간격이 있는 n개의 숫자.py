def solution(x, n):
    answer = []
    m = x
    for i in range(n):
        answer.append(m)
        m += x
        
    return answer