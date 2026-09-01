#입력: s(숫자가 담긴 문자열)
#출력: min_max ("최소값 최대값" 문자열)
"""
1) 공백을 기준으로 s의 숫자를 리스트로 만든다 -> split()
2) 리스트의 값을 순서대로 정렬한다.
3) 첫 번째 값은 최소가 되고, 끝 값은 최대값이 되어 -> 이를 문자열로 만들어 반환한다.
"""
def solution(s):
    nums = list(map(int, s.split(" ")))
    nums.sort()
    return f"{nums[0]} {nums[-1]}"
    
    