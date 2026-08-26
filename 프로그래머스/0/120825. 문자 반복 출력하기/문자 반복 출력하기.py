#입력: my_string(문자열), n(반복할 횟수)
#출력: answer(mystring의 각 문자가 n번만큼 반복된 문자열)
"""
1. 인덱싱을 통해 문자열의 각 문자를 n번 반복한 문자열을 리턴한다.
"""
def solution(my_string, n):
    answer = ""
    for l in my_string:
        answer += l*n
    return answer