#입력: n(정수)
#출력: answer(n의 각 자릿수 숫자 내림차순정렬 문자열)
"""
#변수: temp
1) n의 각 자릿수 값을 배열로 만든다.
2) 그 배열을 sort 함수를 써서 정렬 한다.
3) 그 배열을 문자열로 치환한다.
"""
def solution(n):
    arr = ""
    temp = list(map(int,str(n)))
    # print(temp)
    temp.sort(reverse=True)
    temp = list(map(str, temp))
    for i in temp:
        arr += i
    return int(arr)
    