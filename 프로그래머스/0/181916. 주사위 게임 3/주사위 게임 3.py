#함수명: solution
#함수 기능: 주사위 4개(a,b,c,d)의 경우의 수 5가지에 따른 결과값 반환
#매개변수: a,b,c,d
#리턴값: result

def solution(a,b,c,d):
    result = 0
    nums = [a,b,c,d]
    cnt_nums = [nums.count(x) for x in nums]
    
    #1.p p p p -> 1111*p
    #2.p p p q -> (10*p+q)**2
    #3(1). p p q q -> (p+q) * |p-q|
    #3(2). p p q r -> q*r
    if max(cnt_nums) == 4:
        result = 1111*a
    elif max(cnt_nums) == 3:
        result = (10*nums[cnt_nums.index(3)]+nums[cnt_nums.index(1)])**2
    elif max(cnt_nums) == 2:
        if min(cnt_nums) == 2: #3(1)
            if a == b:
                result = (a+c)*abs(a-c)
            else:
                result = (a+b)*abs(a-b)
        else: #3(2) min(cnt_nums) == 1
            q_and_r = []
            for i, x in enumerate(cnt_nums):
                if x == 1: q_and_r.append(i)
            q = nums[q_and_r[0]]
            r = nums[q_and_r[1]]
            result = q*r
    else:
        result = min(nums)
            
    return result