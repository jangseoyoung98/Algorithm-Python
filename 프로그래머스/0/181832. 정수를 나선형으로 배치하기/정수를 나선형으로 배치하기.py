def solution(n):
    answer = [[0] * n for _ in range(n)]
    
    # 우, 하, 좌, 상 방향 (시계방향)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    x, y, dr = 0, 0, 0
    
    for i in range(1, n * n + 1):
        answer[x][y] = i
        
        # 다음 위치 계산
        nx, ny = x + dx[dr], y + dy[dr]
        
        # 범위를 벗어나거나 이미 채워진 칸인 경우 방향 전환
        if not (0 <= nx < n and 0 <= ny < n and answer[nx][ny] == 0):
            dr = (dr + 1) % 4
            nx, ny = x + dx[dr], y + dy[dr]
            
        x, y = nx, ny
        
    return answer