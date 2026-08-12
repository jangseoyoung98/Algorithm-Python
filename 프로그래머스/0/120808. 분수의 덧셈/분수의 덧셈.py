#입력: numer1, denom1(분수1의 분자/분모) numer2, denom2(분수 2의 분자/분모)
#출력: 배열 answer(두 분수 더한 값을 기약분수로 나타냈을 때의 분자와 분모가 담긴 배열)
"""
기약분수: 분모와 분자의 최대공약수가 1뿐이라서, 더이상 약분할 수 없는 상태의 분수
1) 분수1과 분수2를 더한다.
- 분수1의 분모와 분수2의 분모의 최소공배수를 구한다.
- 그에 맞춰 분수1의 분자와 분수2의 분자를 맞춰서 더한다.
2) 더한 값을 기약분수로 나타낸다.
- 분모와 분자의 최대 공약수를 구한다.
- 분모와 분자 각각을 최대 공약수로 나눈다.
3) answer에 분자와 분모를 넣는다.

1) 두 분수를 무조건 통분하고 -> 최후에 최대공약수만 만들기
(최소공배수를 만드는 건 불필요..)
2) math 라이브러리 안에 최대공약수를 구하는 내장 함수가 있음
"""
import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    sum_numer = numer1*denom2 + numer2*denom1
    sum_denom = denom1*denom2
    
    div = math.gcd(sum_numer, sum_denom)
    answer.append(sum_numer//div)
    answer.append(sum_denom//div)
    
    #최대공약수 구하는 로직 만들어 보기?

    
    
    return answer