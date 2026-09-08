#입력: n (자연수)
#출력: cnt (연속된 자연수로 n을 표현하는 방법의 수)
"""
#변수: 
1) 1부터 n까지의 수열을 만든다.
2) 수열을 순회하며 누적된 합이 n이 되었을 때 cnt에 1을 누적한다.
3) 이렇게 인덱스 한 칸씩 높여가며 순회하고 n까지 갔을 때 끝낸다.
"""
def solution(n):
    cnt = 0 
    add = 0 #합이 n인지 확인하기 위한 임시 값
    nums = [i for i in range(1,n+1)]
    
    for i in range(n):
        add = 0
        while add <= n:
            if add == n:
                cnt += 1
                break
            else:
                add += nums[i]
                i += 1
    return cnt
    