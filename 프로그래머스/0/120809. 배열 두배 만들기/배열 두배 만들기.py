#입력: numbers(정수배열)
#출력: new_numbers(각 인자값이 2배가 된 정수배열)

def solution(numbers):
    new_numbers = [i * 2 for i in numbers] # 컴프리헨션
    
    return new_numbers