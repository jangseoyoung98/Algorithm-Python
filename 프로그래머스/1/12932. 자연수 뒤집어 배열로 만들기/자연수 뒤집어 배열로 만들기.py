#입력: n(자연수)
#출력: arr(n 뒤집힌 숫자 배열)
"""
#변수: arr
1) str()을 써서 문자열로 만든다.
2) 뒤에서부터 하나씩 빼내어 arr에 새로 넣는다. (int 필요!)
"""
def solution(n):
    arr = []
    new_n = str(n)
    for i in range(len(new_n)):
        arr.append(int(new_n[-1-i]))
        # print(arr)
        
    return arr