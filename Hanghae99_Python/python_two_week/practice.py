# N의 값을 입력받습니다. 이 값은 표의 크기이자, 우리가 찾고자 하는 N번째 큰 수를 나타냅니다.
# 최소 힙 (Min-Heap) 초기화:

# N개의 숫자를 저장하기 위해 최소 힙을 사용합니다.
# 최소 힙의 특징을 이용하여, 항상 N개의 가장 큰 숫자만 힙에 유지합니다.
# 숫자 입력과 힙 관리:

# 각 줄에 있는 N개의 숫자를 리스트로 받아들입니다.
# 숫자를 하나씩 읽어오면서, 최소 힙의 크기가 N보다 작은 경우에는 숫자를 힙에 추가합니다.
# 힙의 크기가 N에 도달한 이후에는, 들어온 숫자와 힙의 최솟값을 비교하여 힙을 갱신합니다.
# 최솟값보다 큰 숫자가 들어올 경우, 힙의 최솟값을 제거하고 새로운 숫자를 힙에 추가합니다.
# 이 과정은 N번째 큰 숫자만 힙에 남기게 하여, 마지막에 힙의 최솟값을 출력합니다.
# 결과 출력:

# 힙에 남아있는 N개의 숫자 중 가장 작은 값이 N번째로 큰 숫자이므로, 이를 출력합니다.

import heapq  # 힙 자료구조를 사용하기 위한 heapq 모듈을 임포트합니다.
import sys  # 입력 속도 향상을 위해 sys 모듈을 임포트합니다.

input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline을 사용합니다.

n = int(input())  # 첫 줄에서 N 값을 입력받습니다. 이 값은 표의 크기이자, 우리가 찾고자 하는 N번째 큰 수입니다.
min_heap = []  # 최소 힙을 초기화합니다. N개의 숫자만 유지하기 위해 사용됩니다.

for _ in range(n):  # N번 반복하여 각 행의 숫자들을 처리합니다.
    nums = list(map(int, input().split()))  # 한 행의 N개의 숫자를 입력받아 리스트로 변환합니다.
    
    for num in nums:  # 입력받은 숫자들을 하나씩 처리합니다.
        if len(min_heap) < n:  # 최소 힙의 크기가 N보다 작을 때는 무조건 숫자를 추가합니다.
            heapq.heappush(min_heap, num)  # 힙에 숫자를 추가합니다.
        elif num > min_heap[0]:  # 최소 힙이 이미 N개의 숫자를 갖고 있을 때, 힙의 최솟값보다 큰 숫자가 들어오면,
            heapq.heappop(min_heap)  # 힙에서 최솟값을 제거하고,
            heapq.heappush(min_heap, num)  # 새로운 숫자를 힙에 추가하여 N개의 큰 숫자만 유지합니다.

print(min_heap[0])  # N개의 숫자 중 가장 작은 값, 즉 N번째로 큰 수를 출력합니다.
 
