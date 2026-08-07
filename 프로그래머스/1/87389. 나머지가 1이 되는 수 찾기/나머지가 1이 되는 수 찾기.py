#입력: n(자연수)
#출력: x (n을 x로 나눴을 때 나머지가 1인 가장 작은 자연수)
"""
*원리
항상 나머지가 1 -> n-1의 약수
n-1의 약수 중 가장 작은 수 (1 제외)

*과정
1) n-1의 약수를 구한다.
- 2~n-2까지 or 2~(n-2의 제곱근)까지 나누어 가면서 
딱 떨어지면 약수 / 아니면 패스
2) 딱 떨어지면 바로 리턴한다.
2) 약수 중 1을 제외한 가장 작은 수를 리턴한다. (X)
"""
import math

def solution(n):
    prev = n-1
    # root = math.isqrt(n-1)
    # 소수인 수도 처리해줘야 함!
    for i in range(2,prev+1): #2 ~ prev
        if prev % i == 0:
            return i
    return -1
