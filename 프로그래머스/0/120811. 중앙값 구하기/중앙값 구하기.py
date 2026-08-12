#입력: array (정수 배열)
#출력: answer (array의 중앙값)
"""
★ 배열을 오름차순 한다. -> sorted()
1) array의 갯수를 구한다. 
2) 갯수를 2로 나눠, 중앙값의 인덱스를 구한다.
- array // 2 (올림, +1 하지 않는다. 인덱스는 0에서부터 시작)
3) 해당 인덱스의 값을 반환한다.
"""
def solution(array):
    answer = sorted(array)
    index = len(answer)//2 
    return answer[index]
