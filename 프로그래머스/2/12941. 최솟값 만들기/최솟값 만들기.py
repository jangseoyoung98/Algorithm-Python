#입력: 배열 A,B
#출력: 최소값 minimum (A와 B의 각 원소를 곱한 값을 누적한 것)
"""
*누적값이 최소가 되는 경우: 최소*최대
1) A는 오름차순으로, B는 내림차순으로 정렬한다.
2) A와 B에서 순서대로 원소를 꺼내 곱하고 누적한다.
"""
def solution(A,B):
    new_A = sorted(A)
    new_B = sorted(B, reverse=True)
    index = len(new_A)
    add = 0
    for i in range(index):
        add += new_A[i]*new_B[i]
    return add