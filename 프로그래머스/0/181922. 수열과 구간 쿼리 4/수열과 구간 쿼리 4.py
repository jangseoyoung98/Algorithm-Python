#입력: arr(정수 배열), queries(2차원 정수배열)
#출력: 처리된 arr
"""
query = s i e
1) query를 하나씩 꺼내서, s부터 i까지의 범위의 수를 돌린다.
2) 그 수 중에서 2로 나누었을 때, 나머지가 0이라면 해당 인덱스의 값을 1 올린다.
3) 다 돌고 나서 반환한다.
"""
def solution(arr, queries):
    #for query in queries:
    for s,e,k in queries:
        for i in range(s, e+1): #s~e
            if i%k == 0:
                arr[i] += 1
    
    return arr