
# N = 첫째 줄 연산의 개수, X = 연산에 대한 정보를 나타내는 정수
# X가 자연수이면 배열에 X값을 추가, X가 0이면 최소값을 출력 후에 배열에서 제거, 배열에 값이 없으면 0만 출력 

# 빈배열 생성
# 배열에 0이 아니면 X를 삽입
# 배열 안에 값이 있고 x의 값이 0이면 최소값 출력 후 제거, 배열 안에 값이 없고 x의 값이 0이면 0 출력 


import sys
import heapq

input = sys.stdin.readline

N = int(input().strip())
hq = []

for _ in range(N):
    x = int(input().strip())

    if x > 0:
        heapq.heappush(hq, x)
    else:
        if hq:
            print(heapq.heappop(hq))
        else:
            print(0)

# 메모리 : 37044KB
# 시간 : 108ms