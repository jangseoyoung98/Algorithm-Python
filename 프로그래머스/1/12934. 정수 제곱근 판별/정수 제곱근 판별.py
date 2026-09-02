#입력: n(임의의 양의 정수)
#출력: (x+1)**2 - n이 x의 제곱일 때 / -1 - 없을 때
"""
1) n**0.5 -> 소수점 이하 자리 수가 없다면 O
2) -> 소수점 이하 자리 수가 있다면 -1
"""
def solution(n):
    temp1 = n**0.5
    temp2 = int(temp1)
    if temp1 == temp2:
        return (temp2+1)**2
    else:
        return -1