#입력: numbers - 0~9 숫자들이 들어있는 정수 배열(중복X)
#출력: answer - 0~9까지 중 numbers에 없는 숫자들을 모두 더한 값
"""
1) 0부터 9까지 숫자를 차례로 올려가며 list에 있는지 확인한다.
2) 없으면 answer에 더한다.
3) answer를 반환한다.
"""
def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer += i
    
    return answer