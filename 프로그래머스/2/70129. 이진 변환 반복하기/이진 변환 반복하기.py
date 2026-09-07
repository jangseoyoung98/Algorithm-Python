#입력: 문자열 s
#출력: [time, count] (이진변환 횟수, 제거된 0의 개수)
"""
#변수: count, time, temp
1) 문자열을 순회하며 
- 0이면 count 값을 1씩 증가
- 1이면 temp에 이어붙인다.
2) temp의 길이를 재서 이진수로 표현한다.
*이진수로 바꾸는 방법
- 2로 나누어서 나머지가 없다면 0, 있다면 1
- 몫이 1이 나올 때까지 반복한다.
- 앞서 구해진 수들을 거꾸로 이어 붙인다.
=> temp의 길이가 1이 나올 때까지 반복한다.
"""
def solution(s):
    time,count = 0,0
    temp_s = s # 1과 0으로 이뤄진 문자열

    while True:
        temp = "" # 1로만 이뤄진 문자열

        if temp_s == "1": break

        for l in temp_s:
            if l == "0": 
                count += 1
            else:
                temp += l
        # print(temp) #디버깅
        
        length = len(temp)
        temp_s = ""
        
        quo = length
        while quo > 0:
            if quo%2:
                temp_s += "1"
            else: 
                temp_s += "0"
            quo //= 2
        
        temp_s = temp_s[::-1] #문자열 뒤집기
        time += 1
            
    return [time,count]