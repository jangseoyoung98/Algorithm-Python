def solution(str_list, ex):
    answer = ''

    for l in str_list:
        if ex in l:
            continue
        answer += l
    return answer