#문제이해 : 선입선출이니깐 큐

# 첫 번째 줄 n
# 첫 번째 정보부타 n번째 정보까기 순서대로 처리
# 반복문을 사용하여 a 값 리스트로 생성
# deque를 사용하며 빈배열 생성
# 1이면 list[1]을 대기시킴, 2 이면 left pop시킴 
# print[학생 수가 최대일 때, 학생 수가 최대일 때 뒤에 학생 번호의 수(대기하는 학생의 번호가 여러번이면 맨 뒤에 줄 서 있는 가장 작은 번호의 학생)]

import sys
from collections import deque

input = sys.stdin.readline
queue = deque([])

n = int(input())
max_number = 0
last_number = 0  

for _ in range(n):
    a = list(map(int, input().strip().split()))

    if a[0] == 1: 
        queue.append(a[1]) 

        if len(queue) > max_number:
            max_number = len(queue)
            last_number = queue[-1]  
        elif len(queue) == max_number:
            last_number = min(last_number, queue[-1])

    elif a[0] == 2:  
        queue.popleft() 

print(max_number, last_number)
