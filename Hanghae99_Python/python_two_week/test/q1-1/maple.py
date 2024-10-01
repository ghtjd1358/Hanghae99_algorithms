# 첫 퀘스트 후 첫번째 아케인스톤 활성화 시 500? 
# 세 번째 퀘스트 진행 후 활성화 활성화  300?
# 마지막으로 두 번째 퀘스트 진행 0
# 첫 번째는 2,3째를 더한 값.. 3번 째는 2번째 추가한 경험치를 획득
# 경험치가 적은 퀘스트를 먼저 해야됨

# (300 + 200) + 300

# n = 경험치 수, k = 활성화 수
# 빈배열 생성 
# n만큼 반복문 돌려주고 
# 빈배열에 heap을 사용하여 추가(최소값 순)
# k가 두개 활성이니깐 2개만 남기고 그럼  pop 500 2개만 남으면 또 하나 팝 300 + 800


import sys
import heapq

input = sys.stdin.readline
n, k = map(int, input().strip().split())

results = 0

hq = []

for _ in range(n):
    a = list(map(int, input().strip().split()))

    for b in a:
        heapq.heappush(hq, b)

    if len(hq) >= k:
        heapq.heappop(hq)

        for nums in hq:
            results += nums

print(results)

