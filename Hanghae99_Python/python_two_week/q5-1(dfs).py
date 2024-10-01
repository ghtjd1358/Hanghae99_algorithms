# dfs : 최대한 깊게 방문하지 않은 노드들에 쭉 방문하다가, 더이상 진행할 수 있는 인접정점이 없으면 되돌아감 - 재귀

# 문제 해결 방식
# - 방문 표시를 위해서 입력 받는 그래프의 크기와 똑같은 visit 배열 만들어줌. 
# - 상하좌우 탐색을 위한 direction 001-1선언
# - dfs를 실행하면 방문 표시를 위한 visit에 1로 표시해줌
# - 탐색을 시작한 좌표에 direction을 활용해서 주변 방문
# - 지금까지 방문한 적이 없고, 방문한 곳이 
# 이라면 dfs 실행.. dfs 실행할 때마다 count됨.. 

# 그래프 문제 풀 때
# 2차원 리스트 입력 받기 [list(input().split()) for _ in range(n)]
# direction 0, 0, 1, -1
# 조정한 nx ny는 당연히 r, c 범위 확인


from collections import deque
r,c = map(int, input().split())
pasture = [list(input()) for _ in range(r)]
visit = [[0]*c for _ in range(r)]
d = [(0,1),(0,-1),(1,0),(-1,0)]
cnt = 0

def dfs(x, y) : 
    visit[x][y] = 1
    for dx, dy in d : 
        nx,ny = x+dx, y+dy
        if 0 <= nx < r and 0<= ny < c : 
            if not visit[nx][ny] and pasture[nx][ny] == '#' : 
                dfs(nx, ny)

for x in range(r) : 
    for y in range(c) : 
        # 그래프를 순회하면서 #(clump) 찾기 -> 찾으면 dfs 실행
        if not visit[x][y] and pasture[x][y] == '#' :
            dfs(x, y)
            cnt += 1
print(cnt)