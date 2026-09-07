#입력: 문자열 s
#출력: jaden (jaden case 적용한 문자열)
"""
1) 문자열을 순회하면서 공백이 나오면 스킵, 문자가 나오면 변경한다.
- 앞에 공백 여부를 체크하는 인자: blank - True/False
- 공백이 나오면 blank를 True로, 문자가 나오면 False로 만든다.
2) 문자가 나올 때
- blank가 True인 경우에만 upper() 함수를 씌우고 + blank는 False
- 그 다음 모든 문장은 lower() 함수를 씌운다.
"""
def solution(s):
    jaden = ""
    blank = True
    for l in s:
        if blank and l != " ": #첫 문자는 upper()
            jaden += l.upper()
            blank = False
        elif l == " ": #공백은 그대로 저장
            jaden += l
            blank = True
        else: #나머지는 lower()
            jaden += l.lower()
        
    return jaden