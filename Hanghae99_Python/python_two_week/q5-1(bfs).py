# bfs : 한 노드에서 인접노드까지 방문한 적이 없는 모든 노드를 queue에 삽입. que는 FIFO 방식이라서 순차적인 구현 가능 popleft로 앞에거 빼주면 됨 

# 문제 해결 방식
# - bfs 함수 앞쪽에는 방향, 그래프, 입력, q 정도 선언
# - bfs는 일단 q.append(x,y)와 방문 표시로 시작
# - q를 돌면서 x,y 좌표에는 q에 있는 좌표를 넣어주고.. (popleft)
# - 선언한 방향을 활용해서 nx, ny 좌표를 설정해줌
# - 그리고나서 nx, ny 범위 조건 체크
# - 원하는 조건 확인 & 방문 표시 & q에 방문한 nx, ny 좌표 넣어줌

# 그래프 문제 풀 때
# 2차원 리스트 입력 받기 [list(input().split()) for _ in range(n)]
# direction 0, 0, 1, -1
# 조정한 nx ny는 당연히 r, c 범위 확인


from collections import deque
r,c = map(int, input().split())
pasture = [list(input()) for _ in range(r)]
# 상하좌우
d = [(-1,0), (1,0), (0,-1), (0,1)]
cnt = 0

def bfs(y, x) : 
    # 방문한 적이 없는 노드는 que에 삽입하는ㄱ ㅔ bfs
    # q에 모든 노드 위치를 다 넣고, 방문 표시를 해줌
    q = deque()
    q.append((y,x))
    pasture[y][x] = '1'
    # q를 돌면서 방문한 노드를 체크해줌..
    while q : 
        y,x = q.popleft()
        # 상하좌우 돌기
        for dy, dx in d : 
            Y,X = y+dy, x+dx
            if 0 <= Y < r and 0 <= X < c and pasture[Y][X] == '#' : 
                q.append((Y,X))
                pasture[Y][X] = '1'

for x in range(r) : 
    for y in range(c) : 
        # 그래프를 순회하면서 #(clump) 찾기 -> 찾으면 dfs 실행
        if pasture[x][y] == '#' :
            bfs(x, y)
            cnt += 1
print(cnt)