# 문제 이해 : 최소 힙

# chapter 마다 다른 파일 저장, 
# 소설의 모든 장을 쓰면 합쳐 하나의 파일을 생성, 
# 다 합친 값이 비용
# 2개를 합친 임시파일 생성 또 다른 2개를 합친 임시파일 생성 더 이상 더해줄 원본 챕터가 없으면 임시파일끼리 더한다. 최소 힙을 사용하여 작은 것들부터 나열하고 2개씩 빼내서 더해줌 더한 값을 다시 배열에 추가
# 위에 과정을 list 값이 하나만 남을때까지 반복 
# results 변수를 만들어 빼낸 값들을 더해가면서 계산

# t = 테스트 케이스 
# k = 장의 수
# 빈배열 생성

# k를 반복문으로 돌린다

import sys
import heapq

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    a = list(map(int, input().strip().split()))

    hq = []
    results = 0

    for b in a:
        heapq.heappush(hq, b)
    
    for _ in range(k):
        if len(hq) > 1:
            x = heapq.heappop(hq)
            y = heapq.heappop(hq)
            results += (x+y)
            heapq.heappush(hq, (x+y))
    print(results)


