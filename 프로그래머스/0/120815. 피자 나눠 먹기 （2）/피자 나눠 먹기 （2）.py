#입력: n(사람 수)
#출력: pan(피자 최소 몇 판)
"""
최소 1 ~ 최대 6
6 * pan % n == 0
6 * pan = n의 배수
pan = n의 배수 중 6으로 나누어 떨어지는 최소 수 -> 최소 공배수 // 6
1) n과 6의 최소공배수를 구한다.
2) 그 최소공배수를 6으로 나눈 값을 pan에 넣어서 리턴한다.
"""

def solution(n):
    pan = 0
    lcm = 0
    
    #최대공약수 구하기 -> 그걸로 각 수 나눠서 다 곱하기 = 최소공배수
    for i in range(min(n,6),0, -1):
        if not n%i and not 6%i:
            lcm = i * (n//i) * (6//i)
            break
    pan = lcm // 6

    
    return pan