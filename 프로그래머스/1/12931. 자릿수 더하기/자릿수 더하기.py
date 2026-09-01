#입력: n(자연수)
#출력: val(n의 모든 자릿수의 합)
"""
1. n을 문자열로 만든다.
2. 첫 번째 문자부터 끝 문자까지 int()를 사용해 누적한다.
"""
def solution(n):
    str_n = str(n)
    add = 0
    for l in str_n:
        add += int(l)
    
    return add