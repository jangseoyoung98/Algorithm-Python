"""
함수명: solution
함수 기능: 주사위값 a,b,c,d가 주어졌을 때 5가지 케이스 중 해당하는 점수를 반환
매개변수: a,b,c,d
리턴값: score
"""
#1. 조건1 p p p p -> 1111*p
#2. 조건2 p p p q -> (10*p+q)**2
#3. 조건3 p p q q -> (p+q)*abs(p-q)
#4. 조건4 p p q r -> q * r
#5. 조건5 다 다른 경우 -> 가장 작은 값   

def solution(a,b,c,d):
    temp_list = [a,b,c,d,]
    temp_set = set(temp_list)
    cnt = len(temp_set)

    #1. 네 숫자가 모두 같음
    if cnt == 1:
        return 1111*a

    #2. 숫자가 2 종류인 경우 (3:1 비율 또는 2:2 비율)
    elif cnt == 2:
        # 3:1
        for val in temp_set:
            if temp_list.count(val) == 3:
                p = val
                q = (temp_set - {p}).pop()
                return (10*p+q)**2
        # 2:2
        p,q = list(temp_set)
        return (p+q)*abs(p-q)
    
    #3. 두 주사위만 같고 나머지 두 개는 서로 다름 (2:1:1)
    elif cnt == 3:
        for val in temp_set:
            if temp_list.count(val) == 2:
                # 2번 나온 값(p)을 제외한 나머지 두 값(q,r)의 곱
                q_and_r = [x for x in temp_set if x != val]
                return q_and_r[0]*q_and_r[1]
    #4. 숫자가 모두 다름
    else:
        return min(temp_list)