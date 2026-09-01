#입력: 문자열 s
#출력: T/F (s의 괄호가 제대로 되어 있으면/아니면)
"""
스택(FIFO)과 큐(FILO)
1) 배열에 문자열 s의 괄호를 하나씩 넣는다.
2) 이전에 넣은 것과 쌍을 이루면 빼내고
3) 이전에 넣은 것과 같으면 일단 누적한다.
4) 마지막까지 돌았을 때, 남은 게 없으면 T를 리턴한다.

변수: 임시 배열 temp
"""
def solution(s):
    temp = []
    length = len(s)
    for i in range(length):
        # temp에 아무것도 없다면 일단 누적
        if len(temp) == 0:
            temp.append(s[i])
            continue
        # 다르면서 (일 때는 -> 빼내고
        if s[i] != temp[-1] and temp[-1] == "(":
            temp.pop()
        # 다르면서 )이거나, 같으면 누적하고
        else:
            temp.append(s[i])
    
    if len(temp) == 0:
        return True
    
    return False
