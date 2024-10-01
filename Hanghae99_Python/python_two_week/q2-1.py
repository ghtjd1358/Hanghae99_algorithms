import sys
input = sys.stdin.readline

N = int(input())
stacks = []

for _ in range(N):
    stacks.append(int(input()))

count = 0
current_max = 0

# 스틱을 역순으로 순회
for stack in reversed(stacks):
    if stack > current_max:  # 현재 스틱이 최대 스틱 높이보다 크면
        count += 1  # 카운트를 증가
        current_max = stack  # 현재 최대 스틱 높이 갱신

print(count)  # 남아 있는 스틱 개수 출력


# 아래는 틀린 코드이다

# 접근 방법:
#   빈 배열 생성
#   스틱 추가: appendleft를 사용하여 스틱을 배열에 추가
#   배열이 비어있거나 현재 스틱의 높이가 마지막으로 추가된 스틱보다 클 경우에만 추가
#   역순으로 순회하여 높이 조건을 확인
#   배열의 개수를 확인

import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())

queue = deque([])

sticks = []

for _ in range(N):
    sticks.append(int(input().strip()))

for stick in reversed(sticks):
    if not queue or queue[-1] < stick:
        queue.appendleft(stick)

print(len(queue))
