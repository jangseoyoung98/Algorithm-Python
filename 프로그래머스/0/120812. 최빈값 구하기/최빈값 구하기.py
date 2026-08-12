#입력: array(정수배열)
#출력: answer(최빈값) / -1(최빈값 여러개일 때)

def solution(array):
    arr = sorted(array)
    answer = {}
    cnt = 0

    i = 0
    while i < len(arr): 
        cnt = arr.count(arr[i])
        answer[arr[i]] = cnt
        i += cnt
    
    
    #가장 큰 값을 가진 키 찾기
    #1. 가장 큰 value를 찾기
    #2. 그 value를 가진 키 값을 찾기
    #3. 만약 여러 개라면 -1 반환
    max_value = max(answer.values())
    temp = []
    for k,v in answer.items():
        if max_value == v:
            temp.append(k)
    
    if len(temp) > 1:
        return -1
    
    return temp[0]