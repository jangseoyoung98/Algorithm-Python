#함수명: matchStr -> solution
#함수 기능: 문자열에서 연속된 2개의 같은 단어를 제거해 나갔을 때, 다 사라지면 1 / 아니면 0
#매개변수: 문자열 s
#리턴값: 1(성공) / 0(실패)

def solution(s):
    #1. 빈 리스트(match)를 만들어서, s에서 문자 한 개씩 가져와 집어 넣는다.
    #2. match에 들어있는 값과 같다면 -> pop() 끄집어 내고
    #3. 다르다면 -> append()로 집어 넣는다.
    #4. match의 길이가 0이라면 -> 모든 문자열 제거이므로, return 1 / 아니면 return 0
    
    match = [0] #허수 - s의 첫번째 문자를 집어 넣기 위함
    for l in s:
        if match[-1] == l:
            match.pop()
        else:
            match.append(l)
    if len(match) == 1 : return 1
    else: return 0
    