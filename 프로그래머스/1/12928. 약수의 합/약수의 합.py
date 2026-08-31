#입력: n(정수)
#출력: n의 약수의 합
"""
1) 2부터 제곱근까지 나누어 떨어지는 수를 찾고 누적해서 더한다,
"""
def solution(n):
    #n이 0과 1일때 -> 예외처리
    if n == 0 or n == 1:
        return n
    add = 0

    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            add += i
            #완전제곱수일 때 중복 합계 방지    
            if i != n//i:        
                add += (n//i)    
    return add