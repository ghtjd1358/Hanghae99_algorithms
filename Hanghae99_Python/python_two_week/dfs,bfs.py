# # 입력 : N = 정점의 개수 M = 간선의 개수 V = 시작하는 정점
# # 로직 : DFS ->
# # BFS - >

# # 출력 : DFS 로 출력 한 결과 \n BFS 탐색했을 때 출력


# # input
# N, M, V = map(int, input().split())
# # 1 2 3 4
# graph = [[0]*(N+1) for _ in range(N+1)] # [[0, 0, 0, 0, 0],
# #1 [0, 1, 1, 1, 1],
# #2 [0, 1, 1, 0, 1],
# #3 [0, 1, 0, 1, 1],
# #4 [0, 1, 1, 1, 1]]
# for i in range(M) :
# a, b = map(int, input().split())
# graph[a][b] = graph[b][a] = 1


# # 방문 기록 처리
# visited_bfs = [0]*(N+1)
# visited_dfs = [0]*(N+1) # 0 은 미방문, 1 은 방문


# # dfs 함수
# def dfs(V) : # V =1
# stack = [V] # stack = [1]
# while stack : #vistied_dfs = [0, 0, 0, 0, 0]
# node = stack.pop()
# if not visited_dfs[node] == 1 :
# visited_dfs[node] = 1 #vistied_dfs = [0, 1, 0, 0, 0]
# print(node, end = " ")
# for n in range(N, 0, -1) :
# if graph[node][N] == 1 and visited_dfs[n] == 0 :
# stack.append(n)


# def dfs_재귀(V) :
# visited_dfs[v] = 1
# print(V, end = " ")
# for i in range(1, N+1) :
# if graph[V][i] == 1 and visited_dfs[i] == 0:
# dfs(i)


# # bfs 함수
# def bfs(V) :
# queue = [V]
# while queue :
# node = queue.pop(0)
# visited_bfs[node] = 1
# print(node, end= " ")
# for i in range(1, N+1) :
# if graph[node][i] == 1 and visited_bfs[i] == 0 :
# queue.append(i)