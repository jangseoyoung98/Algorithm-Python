def solution(rny_string):
    answer = ''
    for i in rny_string:
        if i == "m":
            answer += "rn"
            continue
        answer += i
    return answer