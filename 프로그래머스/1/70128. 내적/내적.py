#입력: a,b - 길이가 같은 정수 배열 1,2
#출력: answer - a와 b의 내적
"""
1) zip()으로 동일한 인덱스값끼리 튜플 처리한다.
2) 하나씩 꺼내서 곱하고
3) answer에 더한다.
"""
def solution(a,b):
    answer = 0
    for i,j in zip(a,b):
        answer += i*j
    
    return answer