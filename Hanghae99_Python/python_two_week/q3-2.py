# 1. N개의 입력 값을 받는다
# 2. 빈 배열을 생성 후 값을 배열에 추가한다.
# 3 . list[0]를 기준값으로 정하고 리스트를 순회하며 최댓값이 될때까지 or 최댓값과 같아질때까지 순회한다.
# 4.  기준값이 바뀔때마다 카운팅한다.

import heapq 
import sys

input = sys.stdin.readline 
N = int(input())  # 후보자의 수 입력
others = []  # 다른 후보자들의 득표수를 저장할 최소 힙(하지만 음수로 저장해 최대 힙처럼 사용)
dasom_votes = 0  # 다솜이의 득표수

for i in range(N):
    votes = int(input())  # 각 후보자의 득표수를 입력받음
    if i == 0:
        dasom_votes = votes  # 첫 번째 입력은 다솜이의 득표수로 설정
        #print('첫번째 입력', dasom_votes)
        continue

    heapq.heappush(others, -votes)  # 나머지 후보들의 득표수는 음수로 힙에 저장하여 최대 힙처럼 사용

bribe_count = 0  # 매수해야 하는 유권자의 수를 저장할 변수

while others:  # 힙이 빌 때까지 반복
    votes = -heapq.heappop(others)  # 최대 득표수를 가진 후보의 득표수를 꺼내옴
    if votes < dasom_votes:  # 다솜이의 득표수가 더 많으면 중단
        break

    dasom_votes += 1  # 다솜이의 득표수를 증가
    bribe_count += 1  # 매수한 유권자 수를 증가
    heapq.heappush(others, -(votes - 1))  # 매수한 유권자의 표를 감소시켜 힙에 다시 저장

print(bribe_count)  # 매수해야 하는 최소 유권자 수를 출력

# 메모리 	33188 KB
# 시간      40 ms