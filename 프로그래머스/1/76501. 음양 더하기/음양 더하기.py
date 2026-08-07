#입력: absolutes, signs - 절대값 처리된 정수 배열, 각 정수의 부호(bool - 참 양수/거짓 음수)
#출력: 실제 정수의 합
"""
1) absolutes와 signs에서 각각 하나씩 꺼내서 더해 문자열로 만든다.
  - signs[i]가 true이면 +, false이면 -
2) eval() 함수를 써서 한 번에 계산한다.
"""
def solution(absolutes, signs):
    answer =""
    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += "+"
        else:
            answer += "-"
        answer += str(absolutes[i])
    
    return eval(answer)
