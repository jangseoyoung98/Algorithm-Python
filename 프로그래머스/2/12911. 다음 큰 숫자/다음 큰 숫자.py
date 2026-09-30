#함수명: minNbin-> solution 
#함수 기능: n보다 큰 수 중 가장 작은 수, 이진수 1의 개수는 같은 수를 돌려준다.
#입력: n
#출력: answer
"""
1) while문으로 answer를 구할 때까지 반복한다.
2) n보다 큰 수를 bin()를 적용해 1의 갯수를 찾아내고
- bin(): 이진수 변환 함수 (0b____)
- .count("찾을 문자"): 문자열에서 해당 문자의 개수 반환
3) n과 개수가 같으면 -> break로 빠져나와서 answer를 반환한다.
"""

def solution(n):
    answer = n+1
    bin_n = bin(n).count("1") # n의 1개수
    bin_answer = 0
    
    while True:
        bin_answer = bin(answer).count("1")    
        if bin_answer == bin_n: break
        answer += 1
        
    return answer