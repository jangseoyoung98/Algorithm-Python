#입력: 정수 l, r
#출력: 배열 answer - l~r 사이의 수 중 숫자 0과 5로만 이루어진 모든 정수, 오름차순 배열
"""
* 5를 1, 0을 0 : 이진수
*1. 반복문 범위를 정한다.
*2. 이진수를 0과 5로 바꾸는 방법 -> bin(i) + replace()
*3. l과 r 사이의 값만 걸러내기 및 예외 처리
"""
def solution(l, r):
    answer = []
    temp = []
    for i in range(2**6):
        num = bin(i)
        temp.append(num[2:])
    
    for i in range(len(temp)):
        temp[i] = int(temp[i].replace("1", "5"))
    print(temp)  #확인!
    
    for n in temp:
        if n >= l and n <= r:
            answer.append(n)
    print(answer)

    if not answer:
        return [-1]

    return answer
