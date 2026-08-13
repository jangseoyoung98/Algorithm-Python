#입력: n(정수)
#출력: arr(정수 n 이하의 홀수의 오름차순)
"""
1) 1부터 n까지 +2씩 for문을 돌면서 배열에 append 한다.
"""

def solution(n):
    arr = []
    for i in range(1,n+1,2):
        arr.append(i)
    return arr