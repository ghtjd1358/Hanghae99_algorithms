#문제 이해 : 최대 힙을 구하고 구한 값 적출하여 반토막내고 다시 push 그리고 다시 순회하여 과정들을 반복

# N = 인구수, H = 센티의 키, T = 마법의 뿅망치 횟수 제한 < = 첫번째 줄
# 2번째줄부터 각 거인의 키룰 나타내는 정수 = H
# 센티보다 키가 작도록 할 수 있는 경우 Yes, 두번째 줄에는 최소한의 사용한 횟수를 출력, 반대는 No 이고 가장 큰 키의 거인을 출력
# 키가 1이거나 센티보다 작을 경우 건드리지 않는다.

# 해결 : 1.  빈 list 안에 N개의 수 만큼 값을 추가
#       2.  망치 사용 제한 횟수만큼 배열을 돌린다.
#       3.  heap을 사용하여 최대 힙 값을 빼고 변수에 저장
#       4. 키가 1인 경우 다시 배열에 넣고 break, H보다 값이 적을 경우 다시 배열에 넣고 break  
#       5. heap의 최대값이 센티보다 클 경우 반토막후에 다시 list에 추가
#       6. if문을 사용하여 조건에 맞게 출력

import sys
import heapq

input = sys.stdin.readline

N, H, T = map(int, input().split())

hq = []

cnt = 0

for _ in range(N):
    nums = int(input()) 
    heapq.heappush(hq, -nums) 

for _ in range(T):

    # 가장 큰 거인의 키를 가져옴
    tallest = -heapq.heappop(hq)

    # 키가 1인 경우 더 이상 줄일 수 없으므로 종료
    if tallest == 1:
        heapq.heappush(hq, -tallest) 
        break

    # 키가 센티보다 작으면 종료
    if tallest < H:
        heapq.heappush(hq, -tallest)
        break

    new_height = tallest // 2
    heapq.heappush(hq, -new_height)  

    cnt += 1


tallest = -heapq.heappop(hq)  

if tallest < H:  
    print("YES")  
    print(cnt)   
else:  
    print("NO")   
    print(tallest)  

    
# 메모리 : 	37044KB
# 시간 : 148ms


