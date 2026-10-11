def solution(strArr):
    i = 1
    answer = [ ]
    for l in strArr:
        if i%2: 
            answer.append(l.lower())
        else:
            answer.append(l.upper())
        i += 1
    return answer 