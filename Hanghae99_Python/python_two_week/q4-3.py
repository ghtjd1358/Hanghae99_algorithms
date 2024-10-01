
# 첫 번째 줄은 방문환 횟수 = n, 빈배열 생성
# a = 0이면 아이들을 만남 0인데 선물이 있으면 최대값 pop, 만났으나 선물이 없으면 -1 출력
# 예외의 경우 배열에 선물 push 
# 배열[0]은 선물의 개수니깐 배열[1:]부터 heap 푸시

import sys
import heapq

input = sys.stdin.readline

n = int(input())

hq = []

for _ in range(n):
    a = list(map(int, input().split()))
    
    if a[0] == 0: #아이들을 만난 경우
        if hq:
            print(-heapq.heappop(hq)) #아이들을 만나고 선물이 있는 경우
        else:
            print(-1) #아이들을 만나고 선물이 없는 경우
    else: # 선물을 충전하는 경우
        for charge in a[1:]:
            heapq.heappush(hq, -charge)

# 메모리 : 40920KB
# 시간 : 104ms