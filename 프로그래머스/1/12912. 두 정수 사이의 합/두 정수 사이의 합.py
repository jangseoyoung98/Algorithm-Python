#입력: a,b (두 정수)
#출력: answer (두 정수 사이 모든 값의 합)
"""
1) a와 b가 같다면 a를 리턴
2) a > b라면, range(b,a)로 리스트를 만들고 -> sum
3) 반대라면, 반대
"""

def solution(a,b):
    if a == b:
        return a
    elif a > b:
        return sum([i for i in range(b,a+1)])
    else:
        return sum([i for i in range(a,b+1)])