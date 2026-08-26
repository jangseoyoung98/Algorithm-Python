#입력: num_list(정수 배열)
#출력: answer([짝수 개수, 홀수 개수])
"""
변수: even(짝수 개수), odd(홀수 개수)
1. num_list를 차례로 돌면서 짝수이면 even을 1씩 증가시킨다.
2. 아니면 odd를 1씩 증가시킨다.
3. [even, odd]를 반환한다.
"""
def solution(num_list):
    odd,even = 0,0
    
    for n in num_list:
        if not(n%2):
            even+=1
        else:
            odd+=1

    return [even, odd]