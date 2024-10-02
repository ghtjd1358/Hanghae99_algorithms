# 주어진 숫자판의 크기
n = 5
# 상하좌우 이동을 위한 방향 벡터 정의 (위, 아래, 왼쪽, 오른쪽)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 숫자판 입력 받기
board = [list(map(int, input().split())) for _ in range(n)]

# 6자리 숫자를 저장할 set
result_set = set()

def dfs(x, y, number):
    # 숫자가 6자리가 되면 set에 추가
    if len(number) == 6:
        result_set.add(number)
        # 예시: number = "111111" (6자리가 되었을 때)
        return
    
    # 상하좌우 네 방향으로 이동
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 숫자판을 벗어나지 않는 경우만 탐색
        if 0 <= nx < n and 0 <= ny < n:
            # 예시: 첫 번째 호출 때, number = "1" (첫 번째 위치에서 시작)
            dfs(nx, ny, number + str(board[nx][ny]))
            # 예시: 두 번째 호출 때, number = "11" (상하좌우 중 하나로 이동)

# 5x5 숫자판의 모든 위치에서 DFS 시작
for i in range(n):
    for j in range(n):
        dfs(i, j, str(board[i][j]))
        '''
        예시 1: i=0, j=0, board[0][0] = 1 이므로 처음 시작하는 number는 "1" 
        예시 2: 다음 호출에서는 i=0, j=1, board[0][1] = 1 이므로 number는 "1"
        '''

# 결과 출력 (서로 다른 6자리 수의 개수)
print(len(result_set)) # 결과는 15
'''

과정 예시:

1. DFS 시작: (0, 0) 위치에서 시작 -> number = "1"
   - 상 방향: 갈 수 없음
   - 하 방향: (1, 0) -> number = "11"
     - 상 방향: (0, 0) -> number = "111"
     - 하 방향: (2, 0) -> number = "1111"
     - 좌 방향: 갈 수 없음
     - 우 방향: (1, 1) -> number = "11111"
       - 상 방향: (0, 1) -> number = "111111" (6자리, set에 추가)
       - 하 방향: (2, 1) -> number = "111112" (6자리, set에 추가)
       - 좌 방향: (1, 0) -> number = "111111" (중복)
       - 우 방향: (1, 2) -> number = "111112" (중복)
   - 좌 방향: 갈 수 없음
   - 우 방향: (0, 1) -> number = "11"
     - 이후 상하좌우로 DFS 반복하여 6자리 완성

2. DFS 반복: (0, 1)에서 시작 -> number = "1"
   - 같은 방식으로 6자리 숫자 완성

결국 set에는 총 15개의 서로 다른 6자리 숫자가 저장됨.
'''
